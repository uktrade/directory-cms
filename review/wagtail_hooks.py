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
        ).order_by('-publish_at')[:10]

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


@hooks.register('after_create_page')
@hooks.register('after_edit_page')
def add_page_to_moderation_queue(request, page):
    """
    Add a Moderation record for a Page submitted for moderation

    By default a submission for moderation sets the relevant
    PageRevision.submitted_for_moderation field to True.  However this project
    needs to handle 2i moderation which we've modeled with the Moderation
    object.  We need to ask the user for extra data to create that object so
    this hook sends them to the submit interstitial after a page has been
    created/edited and they clicked "submit for moderation".
    """
    # ignore if the user didn't click "Submit for moderation?"
    is_submitting = bool(request.POST.get('action-submit'))
    if not is_submitting:
        return

    # TODO: use latest() once Django is upgraded to 2.0+
    latest_revision = page.revisions.order_by('-created_at', 'id').first()

    return redirect(
        "moderation-queue:submit_moderation",
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
