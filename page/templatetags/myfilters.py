from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def remove_newlines(widget):

    return mark_safe(str(widget).replace('\n', ' '))