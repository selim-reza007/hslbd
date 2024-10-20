from django import template

register = template.Library()

@register.filter
def contains(value, arg):
    return str(arg) in value