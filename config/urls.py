from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import core.views
import healthcheck.views

api_router = WagtailAPIRouter('api')
api_router.register_endpoint('pages', core.views.PagesOptionalDraftAPIEndpoint)


urlpatterns = [
    url(
        r'^healthcheck/database/$',
        healthcheck.views.DatabaseAPIView.as_view(),
        name='health-check-database'
    ),
    url(
        r'^healthcheck/ping/$',
        healthcheck.views.PingAPIView.as_view(),
        name='health-check-ping'
    ),

    url(
        r'^admin/pages/(?P<pk>[0-9]+)/view_draft/$',
        login_required(core.views.DraftRedirectView.as_view({'get': 'get'})),
        name='draft-view',
    ),

    url(
        r'^admin/pages/(?P<pk>[0-9]+)/copy-to-environment/$',
        login_required(core.views.CopyPageView.as_view()),
        name='copy-to-environment',
    ),
    url(
        (
            r'^admin/pages/preload/(?P<app_name>[a-zA-Z_]+)/'
            r'(?P<model_name>[a-zA-Z]+)/(?P<parent_pk>[0-9]+)/$'
        ),
        login_required(csrf_exempt(core.views.PeloadPageView.as_view())),
        name='preload-add-page',
    ),

    url(r'^api/', api_router.urls),
    url(
        r'^api/pages/lookup-by-type/(?P<page_type>[a-zA-Z\._]+)/',
        api_router.wrap_view(
            core.views.PageLookupByTypeAPIEndpoint.as_view(
                {'get': 'detail_view'}
            )
        ),
        name='lookup-by-page-type'
    ),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
