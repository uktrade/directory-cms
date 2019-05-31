from django.template.loader import render_to_string
from django.urls import reverse
from wagtail.admin.menu import MenuItem
from wagtail.core import hooks

from .models import Moderation


@hooks.register('register_admin_menu_item')
def add_moderation_queue_to_menu():
    return MenuItem(
        'Review',
        reverse('moderation-queue:pending'),
        classnames='icon icon-folder-inverse',
        order=600,
    )


class ModerationQueuePanel:
    order = 200

    def __init__(self, request):
        self.request = request

    def render(self):
        pending = (Moderation.objects.filter(reviews__isnull=True)
                                     .order_by('-created_at')
                                     .select_related('revision', 'revision__user'))
        context = {'pending_moderations': pending}
        return render_to_string(
            'moderation_queue/panel.html',
            context=context,
            request=self.request,
        )


@hooks.register('construct_homepage_panels')
def replace_moderation_panel(request, panels):
    for i, panel in enumerate(panels):
        if panel.name != 'pages_for_moderation':
            continue

        # replace standard Wagtail Moderation panel (PagesForModerationPanel)
        # with a custom panel to show Moderation objects.
        panels[i] = ModerationQueuePanel(request)


@hooks.register('after_create_page')
@hooks.register('after_edit_page')
def add_page_to_moderation_queue(request, page):
    latest_revision = page.revisions.latest('created_at')

    if not latest_revision.submitted_for_moderation:
        return

    # TODO: should we remove exiting Moderation rows for the given page?
    Moderation.objects.create(revision=latest_revision)
