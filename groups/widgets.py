from django.forms.widgets import RadioSelect

from groups import models


class RadioSelectWithGroupInfoModal(RadioSelect):
    template_name = 'groups/widgets/radioselect_with_group_info_modal.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['queryset'] = models.GroupInfo.objects.visibile_to_anyone()
        return context
