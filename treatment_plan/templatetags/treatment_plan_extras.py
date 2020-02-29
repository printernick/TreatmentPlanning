from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def str_to_int(value: str):
    return int(value)

@register.filter
def int_to_str(value: int):
    return str(value)