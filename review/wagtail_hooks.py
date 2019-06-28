from django.conf import settings
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from wagtail.admin.action_menu import ActionMenuItem
from wagtail.admin.menu import MenuItem
from wagtail.core import hooks

from .models import ModerationRequest


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
        # TODO revision__user is not the person who requested the review
        pending = ModerationRequest.objects.pending().exclude(
            revision__user=self.request.user
        ).order_by('-due_date')[:10]

        # Append review URL to each object
        pending = list(pending)
        for moderation in pending:
            moderation.review_url = moderation.get_review_url(self.request.user)

        return render_to_string(
            'moderation_queue/panel.html',
            context={'pending_moderations': pending},
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


@hooks.register('before_create_page')
@hooks.register('before_edit_page')
def disable_wagtail_moderation(request, page):
    """
    When a user hits "submit for moderation" we want it to go through the new moderation workflow.
    We remove 'action-submit' from the POST data so Wagtail doesn't send out any emails pointing to
    the old workflow
    """
    if request.POST:
        request.POST = request.POST.copy()
        request.is_submitting = bool(request.POST.pop('action-submit', False))


@hooks.register('after_create_page')
@hooks.register('after_edit_page')
def add_page_to_moderation_queue(request, page):
    """
    If the user hit "submit for moderation" redirect them to the submit moderation view.
    """
    if request.is_submitting:
        latest_revision = page.revisions.order_by('-created_at', 'id').first()

        return redirect(
            'moderation-queue:submit_moderation',
            pk=latest_revision.id,
        )


@hooks.register('insert_editor_js')
def editor_js():
    js_files = [
        'review/editor.js',
    ]
    js_includes = format_html_join(
        '\n',
        '<script src="{0}{1}"></script>',
        ((settings.STATIC_URL, filename) for filename in js_files)
    )
    return js_includes


# Inject code into the action menu that tells the UI which page is being viewed
# This isn't actually a menu item. It's the only way to inject code into the Wagtail
# editor where we also have the page ID
class GuacamoleMenuItem(ActionMenuItem):
    def render_html(self, request, context):
        return mark_safe(f"<script>window.wagtailPageId = {context['page'].id};</script>")


@hooks.register('register_page_action_menu_item')
def register_guacamole_menu_item():
    return GuacamoleMenuItem(order=10)
