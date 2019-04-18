from django_filters.rest_framework import DjangoFilterBackend

from directory_constants.constants import cms as cms_constants
from rest_framework.exceptions import ValidationError
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from wagtail.admin.api.endpoints import PagesAdminAPIEndpoint
from wagtail.core.models import Orderable, Page, Site

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, Http404
from django.template.response import TemplateResponse
from django.utils import translation
from django.utils.cache import get_conditional_response
from django.views.generic.edit import FormView

from conf.signature import SignatureCheckPermission
from core import cache, filters, forms, helpers, models, permissions, \
    serializers
from core.upstream_serializers import UpstreamModelSerilaizer
from core.serializer_mapping import MODELS_SERIALIZERS_MAPPING


class APIEndpointBase(PagesAdminAPIEndpoint):
    """At the very deep core this is a DRF GenericViewSet, with a few wagtail
    layers on top.

    When all the models will be migrated to DRF serializers we can turn this
    view into a DRF one, removing all the wagtail layers.
    """
    queryset = Page.objects.all()
    meta_fields = []
    known_query_parameters = (
        PagesAdminAPIEndpoint.known_query_parameters.union(
            ['lang', 'draft_token', 'service_name', 'region']
        )
    )

    def get_model_class(self):
        if self.action == 'listing_view':
            model = self.get_queryset().model
        else:
            model = type(self.get_object())
        return model

    def get_serializer_class(self):
        model_class = self.get_model_class()
        return MODELS_SERIALIZERS_MAPPING[model_class]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        region = self.request.GET.get('region')
        if region:
            context['region'] = region
        return context

    @property
    def permission_classes(self):
        permission_classes = [SignatureCheckPermission]
        if helpers.is_draft_requested(self.request):
            permission_classes.append(permissions.DraftTokenPermisison)
        return permission_classes

    def handle_serve_draft_object(self, instance):
        if helpers.is_draft_requested(self.request):
            instance = instance.get_latest_nested_revision_as_page()
        elif not instance.live:
            raise Http404()
        return instance

    def handle_activate_language(self, instance):
        if translation.get_language() not in instance.translated_languages:
            translation.activate(settings.LANGUAGE_CODE)

    def get_object(self):
        instance = super().get_object()
        self.check_object_permissions(self.request, instance)
        instance = self.handle_serve_draft_object(instance)
        self.handle_activate_language(instance)
        return instance


class PagesOptionalDraftAPIEndpoint(APIEndpointBase):
    pass


class DetailViewEndpointBase(APIEndpointBase):
    detail_only_fields = ['id']
    authentication_classes = []
    filter_backends = APIEndpointBase.filter_backends + [DjangoFilterBackend]
    renderer_classes = [JSONRenderer]

    def get_object_id(self):
        """
        Returns the `id` of the requested page. The value is used to
        query `PageCache` for cached response, and by get_object() to
        query the database for a `Page` object. Each subclass must
        override this method to work out the correct `id` value from
        the arguments it receives.

        While this is a slightly roundabout way of identifying pages,
        caches make lookups very cheap, allowing us to identify bad
        parameter combinations early on, at very little cost. Using ids
        for cache lookups also allows `PageCache` to remain simpler and
        more generic, making it useful in more places.

        Raises Http404 when the supplied arguments cannot be matched
        to a page id.
        """
        raise NotImplementedError  # pragma: no cover

    def check_parameter_validity(self):
        """
        Called by `get()` early in the response cycle to give
        the endpoint an opportunity to raise exceptions due to the
        parameters values supplied.
        """
        self.get_object_id()

    def get_object(self):
        if hasattr(self, 'object'):
            return self.object

        # find a page by it's id
        instance = get_object_or_404(
            self.filter_queryset(self.get_queryset()),
            id=self.get_object_id(),
        ).specific

        # check perms or load draft if requested
        self.check_object_permissions(self.request, instance)
        instance = self.handle_serve_draft_object(instance)
        self.handle_activate_language(instance)

        # remember result if requested again
        self.object = instance
        return instance

    def detail_view(self, request, **kwargs):
        # Exit early if there are any issues
        self.check_parameter_validity()

        if helpers.is_draft_requested(request):
            return super().detail_view(request, pk=None)

        # Return a cached response if one is available
        cached_data = cache.PageCache.get(
            page_id=self.get_object_id(),
            lang=translation.get_language(),
            region=request.GET.get('region'),
        )
        if cached_data:
            cached_response = helpers.CachedResponse(cached_data)
            cached_response['etag'] = cached_data.get('etag', None)
            return get_conditional_response(
                request=request,
                etag=cached_response['etag'],
                response=cached_response,
            )

        # No cached response available
        response = super().detail_view(request, pk=None)
        if response.status_code == 200:
            # Reuse the already-fetched object to populate the cache
            cache.CachePopulator.populate_async(self.get_object())

        # No etag is set for this response because creating one is expensive.
        # If API caching is enabled, one will be added to the cached version
        # created above.
        return response


class PageLookupBySlugAPIEndpoint(DetailViewEndpointBase):

    def check_parameter_validity(self):
        # Check 'service_name' was provided
        if 'service_name' not in self.request.GET:
            raise ValidationError(detail={
                'service_name':  "This parameter is required"
            })
        super().check_parameter_validity()

    def get_object_id(self):
        """
        Return the `id` of a relevant Page based on the `service_name` value
        from request.GET and the `slug` parameters from the URL.
        """
        if hasattr(self, 'object_id'):
            return self.object_id

        slug = self.kwargs['slug']
        service_name = self.request.GET['service_name']
        page_id = cache.PageIDCache.get_for_slug(
            slug=slug, service_name=service_name
        )
        if page_id is None:
            raise Http404(
                "No Page found matching service_name '{}' and "
                "slug '{}'".format(service_name, slug)
            )

        self.page_id = page_id
        return page_id


class PageLookupByPathAPIEndpoint(DetailViewEndpointBase):

    def get_object_id(self):
        """
        Return the `id` of a relevant Page based on the `site_id` and `path`
        parameters from the URL. Remembers the outcome for a specific view
        instance to allow free re-retreival.

        A query is needed here to identify the `Site` object for the supplied
        `site_id`, but this will eventually be eliminated by the introduction
        of a dedicated cache for site data.
        """
        if hasattr(self, 'object_id'):
            return self.object_id

        supplied_path = self.kwargs['path'].strip('/')
        full_page_path = self.get_site().root_page.url_path
        # Only combine these if `supplied_path` isn't blank
        if supplied_path:
            full_page_path += supplied_path + '/'

        # Query the cache for a matching `id`
        object_id = cache.PageIDCache.get_for_path(full_page_path)
        if object_id is None:
            raise Http404(
                "No Page found matching site_id '{}' and path '{}'"
                .format(self.kwargs['site_id'], supplied_path)
            )

        self.object_id = object_id
        return object_id

    def get_site(self):
        """
        Find a `Site` matching the `site_id` from the URL.
        """
        if hasattr(self, 'site'):
            return self.site
        site = get_object_or_404(
            Site.objects.all().select_related('root_page'),
            id=self.kwargs['site_id']
        )
        self.site = site
        return site


class PageLookupByFullPathAPIEndpoint(APIEndpointBase):
    lookup_url_kwarg = 'full_path'
    authentication_classes = []

    def get_queryset(self):
        return Page.objects.type(models.BasePage).all()

    def get_object(self):
        if hasattr(self, 'object'):
            return self.object
        if 'full_path' not in self.request.query_params:
            raise ValidationError(
                detail={'full_path': 'This parameter is required'}
            )

        full_path = self.request.query_params['full_path']
        pages = self.get_queryset()
        page = list(filter(lambda x: x.specific.full_path == full_path, pages))
        if page:
            instance = page[0].specific
            self.check_object_permissions(self.request, instance)
            instance = self.handle_serve_draft_object(instance)
            self.handle_activate_language(instance)
            self.object = instance
            return instance
        raise Http404()

    def detail_view(self, *args, **kwargs):
        return super().detail_view(self.request, pk=None)


class UpstreamBaseView(FormView):
    environment_form_class = forms.CopyToEnvironmentForm
    template_name = 'core/upstream.html'

    def get_form_class(self):
        page = self.get_object()
        return page.get_edit_handler().get_form_class()

    def get_object(self):
        if not hasattr(self, 'object'):
            self.object = Page.objects.get(id=self.kwargs['pk']).specific
        return self.object

    def serialize_relations(self):
        instance = self.get_object()
        cluster_data = {}
        for field in instance._meta.related_objects:
            if issubclass(field.related_model, Orderable):
                serialized = map(
                    UpstreamModelSerilaizer.serialize,
                    getattr(instance, field.name).all()
                )
                data = helpers.nested_form_data({
                    field.name: helpers.inline_formset(serialized)
                })
                cluster_data.update(data)
        return cluster_data.items()

    def serialize_object(self):
        instance = self.get_object()
        return UpstreamModelSerilaizer.serialize(instance).items()

    def get_context_data(self, **kwargs):
        page = self.get_object()
        return super().get_context_data(
            environment_form=self.environment_form_class(),
            page=page,
            service_name=page._meta.app_label,
            model_name=page._meta.model_name,
            serialized_relations=self.serialize_relations(),
            serialized_object=self.serialize_object(),
            parent_slug=page.specific.get_parent().slug,
            **kwargs
        )


class CopyUpstreamView(UpstreamBaseView):
    pass


class UpdateUpstreamView(UpstreamBaseView):
    pass


class PreloadPageView(FormView):
    template_name = 'wagtailadmin/pages/create.html'
    update_template_name = 'wagtailadmin/pages/edit.html'
    filter_class = filters.ServiceNameDRFFilter
    http_method_names = ['post']

    def dispatch(self, *args, **kwargs):
        self.page_content_type = self.get_page_content_type()
        self.page = self.get_page()
        try:
            return super().dispatch(*args, **kwargs)
        except ValidationError as error:
            return HttpResponseBadRequest(error)

    def get_page_content_type(self):
        try:
            return ContentType.objects.get_by_natural_key(
                self.kwargs['service_name'],
                self.kwargs['model_name'],
            )
        except ContentType.DoesNotExist:
            raise Http404()

    def get_page(self):
        page_class = self.page_content_type.model_class()
        try:
            page = page_class.objects.get(
                slug=self.request.POST.get('slug'),
                service_name__iexact=self.kwargs['service_name']
            )
        except page_class.DoesNotExist:
            page = page_class()
        page.owner = self.request.user
        return page

    def get_form_class(self):
        page_class = self.page_content_type.model_class()
        return page_class.get_edit_handler().get_form_class()

    def get_parent(self):
        queryset = filters.ServiceNameFilter().filter_service_name(
            queryset=Page.objects.all(),
            name=None,
            value=self.kwargs['service_name'].upper(),
        )
        return get_object_or_404(
            queryset,
            slug=self.kwargs['parent_slug'],
        ).specific

    def get_context_data(self, form):
        page_class = self.page_content_type.model_class()
        parent_page = self.get_parent()
        edit_handler = page_class.get_edit_handler()
        form_class = edit_handler.get_form_class()
        form = form_class(
            data=form.data,
            instance=self.page,
            parent_page=parent_page,
        )
        edit_handler = edit_handler.bind_to_instance(
            instance=self.page,
            form=form,
            request=self.request
        )
        return {
            'content_type': self.page_content_type,
            'page_class': page_class,
            'parent_page': parent_page,
            'edit_handler': edit_handler,
            'preview_modes': self.page.preview_modes,
            'form': form,
            'has_unsaved_changes': True,
            'page': self.page,
            'page_for_status': self.page,
            **super().get_context_data(form=form),
        }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        data = UpstreamModelSerilaizer.deserialize(
            kwargs['data'], request=self.request
        )
        kwargs['data'] = data
        return kwargs

    def form_valid(self, form):
        return TemplateResponse(
            self.request,
            self.get_template_names(),
            self.get_context_data(form=form),
        )

    def get_template_names(self):
        if self.page.pk:
            return [self.update_template_name]
        return [self.template_name]


class PageTypeView(APIView):
    permission_classes = [SignatureCheckPermission]

    def _build_model_string(self, model_class):
        content_type_object = ContentType.objects.get_for_model(model_class)
        return '{app}.{model}'.format(
            app=content_type_object.app_label,
            model=content_type_object.model
        )

    def get(self, request, format=None):
        data = {
            'types': [self._build_model_string(item) for
                      item in MODELS_SERIALIZERS_MAPPING]
        }
        serializer = serializers.PagesTypesSerializer(data=data)
        serializer.is_valid()
        return Response(serializer.data)
