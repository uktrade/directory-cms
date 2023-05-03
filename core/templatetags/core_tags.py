from django import template


register = template.Library()


@register.filter("not_string")
def not_string(bound_field):
    return isinstance(bound_field, str)