from django.views.generic import ListView

from .models import PagePendingModeration


class PendingModerations(ListView):
    model = PagePendingModeration
    template_name = "moderation_queue/list.html"
