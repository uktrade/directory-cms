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
from groups.views import GroupInfoModalView

api_router = WagtailAPIRouter('api')
api_router.register_endpoint('pages', core.views.PagesOptionalDraftAPIEndpoint)


api_urls = [
    url(r'^', api_router.urls),
    url(
        r'^pages/lookup-by-slug/(?P<slug>[\w-]+)/',
        api_router.wrap_view(core.views.PageLookupBySlugAPIEndpoint.as_view({'get': 'detail_view'})),
        name='lookup-by-slug'
    ),
    url(
        r'^pages/lookup-by-path/(?P<site_id>[0-9]+)/(?P<path>[\w\-/]*)$',
        api_router.wrap_view(core.views.PageLookupByPathAPIEndpoint.as_view({'get': 'detail_view'})),
        name='lookup-by-path'
    ),
    url(
        r'^pages/types/$',
        core.views.PageTypeView.as_view(),
        name='pages-types-list'
    ),
    url(
        r'^pages/lookup-countries-by-tag/(?P<pk>[0-9]+)/$',
        api_router.wrap_view(export_readiness.views.CountryPageLookupByIndustryTagIDListAPIView.as_view()),
        name='lookup-countries-by-tag-list'
    ),
    url(
        r'^pages/industry-tags/$',
        api_router.wrap_view(export_readiness.views.IndustryTagsListAPIView.as_view()),
        name='industry-tags-list'
    ),
    url(
        r'^pages/lookup-countries/$',
        api_router.wrap_view(export_readiness.views.CountryPageListAPIView.as_view()),
        name='lookup-country-guides-list-view'
    ),
    url(
        r'^regions/$',
        api_router.wrap_view(export_readiness.views.RegionsListAPIView.as_view()),
        name='regions-list-view'
    ),
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
        include((api_urls, 'api'))
    ),
    url(
        r'^healthcheck/',
        include((healthcheck_urls, 'healthcheck'))
    ),
    url(
        r'^$',
        RedirectView.as_view(url='/admin/')
    ),
    url(
        r'^admin/pages/(?P<pk>[0-9]+)/copy-upstream/$',
        login_required(core.views.CopyUpstreamView.as_view(is_edit=False)),
        name='copy-upstream',
    ),
    url(
        r'^admin/pages/(?P<pk>[0-9]+)/update-upstream/$',
        login_required(core.views.UpdateUpstreamView.as_view(is_edit=True)),
        name='update-upstream',
    ),
    url(
        r'^admin/pages/preload/',
        csrf_exempt(core.views.PreloadPageView.as_view()),
        name='preload-add-page',
    ),
    url(r'^admin/group-info/$', login_required(GroupInfoModalView.as_view()), name='group-info'),

    # Prevent users from changing their email address
    url(r'^admin/account/change_email/$', RedirectView.as_view(url='/admin/')),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^auth/request-access/', include('users.urls_sso')),
    url(r'^activity-stream/v1/', ActivityStreamView.as_view(), name='activity-stream'),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.FEATURE_FLAGS['ENFORCE_STAFF_SSO_ON']:
    urlpatterns = [
        url('^auth/', include('authbroker_client.urls')),
        url(r'^admin/login/$', RedirectView.as_view(url='/auth/login/', query_string=True)),
    ] + urlpatterns


if settings.FEATURE_FLAGS['DEBUG_TOOLBAR_ON']:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
