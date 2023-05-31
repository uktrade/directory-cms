import directory_components.views
from directory_components.decorators import skip_ga360
import directory_healthcheck.views
from django.contrib import admin
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import RedirectView
from django.urls import path, re_path

import core.views
from groups.views import GroupInfoModalView

api_router = WagtailAPIRouter('api')
api_router.register_endpoint('pages', core.views.PagesOptionalDraftAPIEndpoint)


api_urls = [
    re_path(r'^', api_router.urls),
    re_path(
        r'^pages/lookup-by-slug/(?P<slug>[\w-]+)/',
        api_router.wrap_view(core.views.PageLookupBySlugAPIEndpoint.as_view({'get': 'detail_view'})),
        name='lookup-by-slug',
    ),
    re_path(
        r'^pages/lookup-by-path/(?P<site_id>[0-9]+)/(?P<path>[\w\-/]*)$',
        api_router.wrap_view(core.views.PageLookupByPathAPIEndpoint.as_view({'get': 'detail_view'})),
        name='lookup-by-path',
    ),
    re_path(r'^pages/types/$', core.views.PageTypeView.as_view(), name='pages-types-list'),
]


healthcheck_urls = [
    re_path(r'^$', directory_healthcheck.views.HealthcheckView.as_view(), name='healthcheck'),
    re_path(r'^ping/$', directory_healthcheck.views.PingView.as_view(), name='ping'),
]


urlpatterns = [
    re_path(r'^django-admin/', admin.site.urls),
    re_path(r'^api/', include((api_urls, 'api'))),
    re_path(r'^healthcheck/', include((healthcheck_urls, 'healthcheck'))),
    re_path(
        r"^robots\.txt$",
        skip_ga360(directory_components.views.RobotsView.as_view(template_name='core/robots.txt')),
        name='robots',
    ),
    re_path(r'^$', RedirectView.as_view(url='/admin/')),
    re_path(
        r'^admin/pages/(?P<pk>[0-9]+)/copy-upstream/$',
        login_required(core.views.CopyUpstreamView.as_view(is_edit=False)),
        name='copy-upstream',
    ),
    re_path(
        r'^admin/pages/(?P<pk>[0-9]+)/update-upstream/$',
        login_required(core.views.UpdateUpstreamView.as_view(is_edit=True)),
        name='update-upstream',
    ),
    re_path(
        r'^admin/pages/preload/',
        login_required(csrf_exempt(core.views.PreloadPageView.as_view())),
        name='preload-add-page',
    ),
    re_path(r'^admin/group-info/$', login_required(GroupInfoModalView.as_view()), name='group-info'),
    # Prevent users from changing their email address
    re_path(r'^admin/account/change_email/$', RedirectView.as_view(url='/admin/')),
    re_path(r'^admin/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^auth/request-access/', include('users.urls_sso')),
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    re_path(r'', include(wagtail_urls)),
    path(
        'subtitles/<int:great_media_id>/<str:language>/content.vtt',
        core.views.serve_subtitles,
        name='subtitles-serve',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.FEATURE_FLAGS['ENFORCE_STAFF_SSO_ON']:
    urlpatterns = [
        re_path('^auth/', include('authbroker_client.urls')),
        re_path(r'^admin/login/$', RedirectView.as_view(url='/auth/login/', query_string=True)),
    ] + urlpatterns


if settings.FEATURE_FLAGS['DEBUG_TOOLBAR_ON']:
    import debug_toolbar

    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
