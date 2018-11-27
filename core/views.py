import json
import logging

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.exceptions import ValidationError
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import JSONRenderer
from wagtail.admin.api.endpoints import PagesAdminAPIEndpoint
from wagtail.core.models import Page
from wagtail.core.models import Orderable

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, Http404
from django.template.response import TemplateResponse
from django.utils import translation
from django.utils.cache import get_conditional_response, set_response_etag
from django.views.generic.edit import FormView

from conf.signature import SignatureCheckPermission
from core import filters, forms, helpers, permissions
from core.cache import is_registered_for_cache, PageCache
from core.models import BasePage
from core.upstream_serializers import UpstreamModelSerilaizer
from export_readiness import models as ex_read_models
from export_readiness import serializers as ex_read_serializers
from invest import models as invest_models
from invest import serializers as invest_serializers


logger = logging.getLogger(__name__)


MODELS_SERIALIZERS_MAPPING = {
    # export readiness
    ex_read_models.TermsAndConditionsPage: ex_read_serializers.GenericBodyOnlyPageSerializer,  # NOQA
    ex_read_models.PrivacyAndCookiesPage: ex_read_serializers.GenericBodyOnlyPageSerializer,  # NOQA
    ex_read_models.GetFinancePage: ex_read_serializers.GetFinancePageSerializer,  # NOQA
    ex_read_models.PerformanceDashboardPage: ex_read_serializers.PerformanceDashboardPageSerializer,  # NOQA
    ex_read_models.PerformanceDashboardNotesPage: ex_read_serializers.GenericBodyOnlyPageSerializer,  # NOQA
    ex_read_models.ArticlePage: ex_read_serializers.ArticlePageSerializer,
    ex_read_models.HomePage: ex_read_serializers.HomePageSerializer,
    ex_read_models.ArticleListingPage: ex_read_serializers.ArticleListingPageSerializer,  # NOQA
    ex_read_models.TopicLandingPage: ex_read_serializers.TopicLandingPageSerializer,  # NOQA
    ex_read_models.InternationalLandingPage: ex_read_serializers.InternationalLandingPageSerializer,  # NOQA
    ex_read_models.CampaignPage: ex_read_serializers.CampaignPageSerializer,
    # invest
    invest_models.SectorLandingPage: invest_serializers.SectorLandingPageGenericSerializer,  # NOQA
    invest_models.RegionLandingPage: invest_serializers.SectorLandingPageGenericSerializer,  # NOQA
    invest_models.SectorPage: invest_serializers.SectorPageSerializer,
    invest_models.SetupGuideLandingPage: invest_serializers.SetupGuideLandingPageSerializer,  # NOQA
    invest_models.SetupGuidePage: invest_serializers.SetupGuidePageSerializer,
    invest_models.InvestHomePage: invest_serializers.InvestHomePageSerializer,
    invest_models.InfoPage: invest_serializers.InfoPageSerializer,
    invest_models.HighPotentialOpportunityFormPage: invest_serializers.HighPotentialOpportunityFormPageSerializer,  # NOQA
    invest_models.HighPotentialOpportunityDetailPage: invest_serializers.HighPotentialOpportunityDetailPageSerializer,  # NOQA
    invest_models.HighPotentialOpportunityFormSuccessPage: invest_serializers.HighPotentialOpportunityFormSuccessPageSerializer,  # NOQA
    # find a supplier
}


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
            ['lang', 'draft_token', 'service_name']
        )
    )

    def get_model_class(self):
        # Get model
        if self.action == 'listing_view':
            model = self.get_queryset().model
        else:
            model = type(self.get_object())
        return model

    def get_serializer_class(self):
        model_class = self.get_model_class()
        if model_class in MODELS_SERIALIZERS_MAPPING:
            return MODELS_SERIALIZERS_MAPPING[model_class]
        else:
            return super().get_serializer_class()

    @classmethod
    def get_nested_default_fields(cls, model):
        fields = [field.name for field in model.api_fields]
        # "other_opportunites" prevents the field being serialized
        # for `HighPotentialOpportunityDetailPage`, which results in
        # infinite recursion.
        if model == HighPotentialOpportunityDetailPage:
            fields.remove('other_opportunities')
        elif model == SectorPage:
            fields.remove('children_sectors')
        return fields

    @classmethod
    def get_listing_default_fields(cls, model):
        return [field.name for field in model.api_fields]

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


class PageLookupBySlugAPIEndpoint(APIEndpointBase):
    lookup_url_kwarg = 'slug'
    detail_only_fields = ['id']
    filter_backends = APIEndpointBase.filter_backends + [DjangoFilterBackend]
    filter_class = filters.ServiceNameDRFFilter
    authentication_classes = []
    renderer_classes = [JSONRenderer]

    def dispatch(self, *args, **kwargs):
        if (
            'service_name' not in self.request.GET or
            helpers.is_draft_requested(self.request)
        ):
            return super().dispatch(*args, **kwargs)
        cached_page = PageCache.get(
            slug=self.kwargs['slug'],
            service_name=self.request.GET['service_name'],
            language_code=translation.get_language()
        )
        if cached_page:
            etag = cached_page.get('etag', None)
            cached_response = helpers.CachedResponse(cached_page)
            cached_response['etag'] = etag
            response = get_conditional_response(
                request=self.request,
                etag=etag,
                response=cached_response,
            )
        else:
            response = super().dispatch(*args, **kwargs)
            model = self.get_object().__class__
            if is_registered_for_cache(model) and response.status_code == 200:
                response.render()
                set_response_etag(response)
                PageCache.set(
                    slug=self.kwargs['slug'],
                    language_code=translation.get_language(),
                    service_name=self.request.GET['service_name'],
                    contents={
                        **json.loads(response.content),
                        'etag': response.get('ETag')
                    }
                )
        return response

    def get_queryset(self):
        return Page.objects.all()

    def get_object(self):
        if hasattr(self, 'object'):
            return self.object
        if 'service_name' not in self.request.query_params:
            raise ValidationError(
                detail={'service_name': 'This parameter is required'}
            )
        instance = get_object_or_404(
            self.filter_queryset(self.get_queryset()),
            slug=self.kwargs['slug'],
        ).specific
        self.check_object_permissions(self.request, instance)
        instance = self.handle_serve_draft_object(instance)
        self.handle_activate_language(instance)
        self.object = instance
        return instance

    def detail_view(self, *args, **kwargs):
        return super().detail_view(self.request, pk=None)


class PageLookupByFullPathAPIEndpoint(APIEndpointBase):
    lookup_url_kwarg = 'full_path'
    authentication_classes = []

    def get_queryset(self):
        return Page.objects.type(BasePage).all()

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


class PageLookupByTagListAPIEndpoint(RetrieveAPIView):
    queryset = ex_read_models.Tag
    serializer_class = ex_read_serializers.TagSerializer
    lookup_field = 'slug'


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
        return super().dispatch(*args, **kwargs)

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
        data = UpstreamModelSerilaizer.deserialize(kwargs['data'])
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
