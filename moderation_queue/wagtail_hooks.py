from django.template.loader import render_to_string
from django.urls import reverse
from wagtail.admin.menu import MenuItem
from wagtail.core import hooks

from .models import PagePendingModeration


@hooks.register('register_admin_menu_item')
def add_moderation_queue_to_menu():
    return MenuItem(
        'Moderation Queue',
        reverse('moderation-queue'),
        classnames='icon icon-folder-inverse',
        order=600,
    )


class ModerationQueuePanel:
    order = 200

    def render(self):
        pending_moderations = (PagePendingModeration.objects.order_by('-created_at')
                                                            .select_related('revision', 'user'))
        context = {'pending_moderations': pending_moderations}
        return render_to_string('moderation_queue/panel.html', context=context)


@hooks.register('construct_homepage_panels')
def replace_moderation_panel(request, panels):
    for i, panel in enumerate(panels):
        if panel.name != 'pages_for_moderation':
            continue

        # replace standard Wagtail Moderation panel (PagesForModerationPanel)
        # with a custom panel to show PagePendingModeration objects.
        panels[i] = ModerationQueuePanel()
