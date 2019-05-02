import directory_healthcheck.views
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import RedirectView

import core.views
import export_readiness.views
from activitystream.views import ActivityStreamView

api_router = WagtailAPIRouter('api')
api_router.register_endpoint('pages', core.views.PagesOptionalDraftAPIEndpoint)


api_urls = [
    url(r'^', api_router.urls),
    url(
        r'^pages/lookup-by-slug/(?P<slug>[\w-]+)/',
        api_router.wrap_view(
            core.views.PageLookupBySlugAPIEndpoint.as_view(
                {'get': 'detail_view'}
            )
        ),
        name='lookup-by-slug'
    ),
    url(
        r'^pages/lookup-by-path/(?P<site_id>[0-9]+)/(?P<path>[\w\-/]*)$',
        api_router.wrap_view(
            core.views.PageLookupByPathAPIEndpoint.as_view(
                {'get': 'detail_view'}
            )
        ),
        name='lookup-by-path'
    ),
    url(
        r'^pages/lookup-by-tag/(?P<slug>[\w-]+)/$',
        api_router.wrap_view(
            export_readiness.views.PageLookupByTagListAPIEndpoint.as_view()
        ),
        name='lookup-by-tag-list'
    ),
    url(
        r'^pages/types/$',
        core.views.PageTypeView.as_view(),
        name='pages-types-list'
    )
]


healthcheck_urls = [
    url(
        r'^$',
        directory_healthcheck.views.HealthcheckView.as_view(),
        name='healthcheck'
    ),
    url(
        r'^ping/$',
        directory_healthcheck.views.PingView.as_view(),
        name='ping'
    ),
]


urlpatterns = [
    url(
        r'^api/',
        include(api_urls, namespace='api', app_name='api')
    ),
    url(
        r'^healthcheck/',
        include(
            healthcheck_urls, namespace='healthcheck', app_name='healthcheck'
        )
    ),
    url(
        r'^$',
        RedirectView.as_view(url='/admin/')
    ),
    url(
        r'^admin/pages/(?P<pk>[0-9]+)/copy-upstream/$',
        login_required(core.views.CopyUpstreamView.as_view()),
        name='copy-upstream',
    ),
    url(
        r'^admin/pages/(?P<pk>[0-9]+)/update-upstream/$',
        login_required(core.views.UpdateUpstreamView.as_view()),
        name='update-upstream',
    ),
    url(
        (
            r'^admin/pages/preload/(?P<service_name>[a-zA-Z_]+)/'
            r'(?P<model_name>[a-zA-Z]+)/(?P<parent_slug>[a-zA-Z-]+)/$'
        ),
        login_required(csrf_exempt(core.views.PreloadPageView.as_view())),
        name='preload-add-page',
    ),

    # Prevent users from changing their email address
    url(r'^admin/account/change_email/$', RedirectView.as_view(url='/admin/')),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(
        r'^activity-stream/v1/',
        ActivityStreamView.as_view(),
        name='activity-stream'
    ),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.FEATURE_FLAGS['DEBUG_TOOLBAR_ON']:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
