from django import forms
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.html import format_html

from groups.models import GroupInfo


class GroupChoiceFieldWithRolesModal(forms.ModelChoiceField):
    def __init__(self, *args, **kwargs):
        if 'queryset' not in kwargs:
            kwargs['queryset'] = Group.objects.filter(
                info__visibility=GroupInfo.VISIBILITY_UNRESTRICTED
            )

        kwargs['queryset'] = (
            kwargs['queryset'].select_related('info')
            .order_by('info__seniority_level', 'info__name_singular')
        )
        super().__init__(*args, **kwargs)

    def get_bound_field(self, form, field_name):
        # Overriding help_text here because forms are loaded before
        # urls are ready
        self.help_text = format_html(
            '<a href="{url}" class="action-view-group-info">'
            'Not sure which role to choose?</a>',
            url=reverse('group-info')
        )
        return super().get_bound_field(form, field_name)

    def label_from_instance(self, obj):
        return obj.info.name_singular


class GroupWithSummariesMultipleChoiceField(forms.ModelMultipleChoiceField):
    def __init__(self, *args, **kwargs):
        kwargs['queryset'] = kwargs['queryset'].select_related('info')
        return super().__init__(*args, **kwargs)

    def label_from_instance(self, obj):
        return format_html(
            '<b>{name}</b> {permission_summary}',
            name=obj.name, permission_summary=obj.info.permission_summary,
        )
