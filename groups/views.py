from django.views import generic
from wagtail.admin.modal_workflow import render_modal_workflow

from groups.models import GroupInfo


class GroupInfoModalView(generic.TemplateView):

    def get(self, request):
        return render_modal_workflow(
            request, 'wagtailadmin/groups/group_info_modal.html', None, {
                'queryset': GroupInfo.objects.visible_to_user(request.user),
            }
        )
