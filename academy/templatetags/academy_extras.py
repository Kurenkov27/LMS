from django import template

register = template.Library()


@register.filter()
def get_count(value):
    return value.count()
