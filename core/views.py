from rest_framework.exceptions import ValidationError
from wagtail.admin.api.endpoints import PagesAdminAPIEndpoint
from wagtail.core.models import Page
from wagtail.core.models import Orderable

from django.conf import settings
from django.contrib.contenttypes.models import ContentType

from django.shortcuts import get_object_or_404, Http404
from django.template.response import TemplateResponse
from django.utils import translation
from django.views.generic.edit import FormView

from conf.signature import SignatureCheckPermission
from core import forms, helpers, permissions
from core.upstream_serializers import UpstreamModelSerilaizer


class APIEndpointBase(PagesAdminAPIEndpoint):
    queryset = Page.objects.all()
    meta_fields = []
    known_query_parameters = (
        PagesAdminAPIEndpoint.known_query_parameters.union(
            ['lang', 'draft_token', 'service_name']
        )
    )

    @classmethod
    def get_nested_default_fields(cls, model):
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

    def get_queryset(self):
        return Page.objects.all()

    def get_object(self):
        if 'service_name' not in self.request.query_params:
            raise ValidationError(
                detail={'service_name': 'This parameter is required'}
            )
        instance = get_object_or_404(
            self.get_queryset(),
            historicslug__slug=self.kwargs['slug'],
            service__name=self.request.query_params['service_name']
        ).specific
        self.check_object_permissions(self.request, instance)
        instance = self.handle_serve_draft_object(instance)
        self.handle_activate_language(instance)
        return instance

    def detail_view(self, *args, **kwargs):
        return super().detail_view(self.request, pk=None)


class UpstreamBaseView(FormView):
    environment_form_class = forms.CopyToEnvironmentForm
    template_name = 'core/upstream.html'

    include_slug = None

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
            app_label=page._meta.app_label,
            model_name=page._meta.model_name,
            serialized_relations=self.serialize_relations(),
            serialized_object=self.serialize_object(),
            include_slug=self.include_slug,
            **kwargs
        )


class CopyUpstreamView(UpstreamBaseView):
    include_slug = False


class UpdateUpstreamView(UpstreamBaseView):
    include_slug = True


class PreloadPageView(FormView):
    template_name = 'wagtailadmin/pages/create.html'
    update_template_name = 'wagtailadmin/pages/edit.html'

    def dispatch(self, *args, **kwargs):
        self.page_content_type = self.get_page_content_type()
        self.page = self.get_page()
        return super().dispatch(*args, **kwargs)

    def get_page_content_type(self):
        try:
            return ContentType.objects.get_by_natural_key(
                self.kwargs['app_name'],
                self.kwargs['model_name'],
            )
        except ContentType.DoesNotExist:
            raise Http404()

    def get_page(self):
        page_class = self.page_content_type.model_class()
        try:
            page = page_class.objects.get(
                slug=self.request.POST.get('slug_en_gb')
            )
        except page_class.DoesNotExist:
            page = page_class()
        page.owner = self.request.user
        return page

    def get_form_class(self):
        page_class = self.page_content_type.model_class()
        return page_class.get_edit_handler().get_form_class()

    def get_parent(self):
        return get_object_or_404(Page, id=self.kwargs['parent_pk']).specific

    def get_context_data(self, form):
        page_class = self.page_content_type.model_class()
        parent_page = self.get_parent()
        edit_handler = page_class.get_edit_handler()
        form_class = edit_handler.get_form_class()
        form = form_class(
            data=form.data,
            instance=self.page,
            parent_page=parent_page
        )
        edit_handler = edit_handler.bind_to_instance(
            instance=self.page,
            form=form
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
            self.template_name,
            self.get_context_data(form=form),
        )

    def get_template_names(self):
        if self.page.pk:
            return [self.update_template_name]
        return [self.template_name]
