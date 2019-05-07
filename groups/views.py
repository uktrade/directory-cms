from django.views import generic
from groups.models import GroupInfo


class GroupInfoModalView(generic.TemplateView):
    template_name = "wagtailadmin/groups/group_info_modal.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(
            queryset=GroupInfo.objects.visible_to_user(self.request.user)
        )
