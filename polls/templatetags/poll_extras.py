from django import template

register = template.Library()

@register.filter(name="teste")

def filter_teste(value):
    return "{} + .".format(value)