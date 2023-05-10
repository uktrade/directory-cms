from django import template


register = template.Library()


@register.filter("can_render")
def can_render(bound_field):
    return hasattr(bound_field, 'field')
