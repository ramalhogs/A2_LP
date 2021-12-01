from django import template

register = template.Library()

@register.filter(name="teste")

def ponto_final(value):
    return "{}.".format(value)

