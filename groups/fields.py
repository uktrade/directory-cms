from django import forms
from django.urls import reverse
from django.utils.html import format_html

from groups.models import GroupInfo


class RoleChoiceField(forms.ModelChoiceField):
    """
    Use as ModelChoiceField to the Group model to get options powered
    by a GroupInfoQuerySet - which provides singular names as labels,
    and more natural ordering (by seniority)
    """
    def __init__(self, *args, **kwargs):
        if 'queryset' not in kwargs:
            kwargs['queryset'] = GroupInfo.objects.visible_to_anyone()
        kwargs['to_field_name'] = 'group_id'
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        val = super().to_python(value)
        if isinstance(val, GroupInfo):
            return val.group
        return val

    def get_bound_field(self, form, field_name):
        # Overriding help_text here because forms are loaded before
        # urls are ready
        self.help_text = format_html(
            '<a href="{url}" class="action-view-group-info">'
            'Not sure which role to choose?</a>',
            url=reverse('group-info')
        )
        return super().get_bound_field(form, field_name)


class GroupWithSummariesMultipleChoiceField(forms.ModelMultipleChoiceField):
    def __init__(self, *args, **kwargs):
        kwargs['queryset'] = kwargs['queryset'].select_related('info')
        return super().__init__(*args, **kwargs)

    def label_from_instance(self, obj):
        return format_html(
            '<b>{name}</b> {permission_summary}',
            name=obj.name, permission_summary=obj.info.permission_summary,
        )
