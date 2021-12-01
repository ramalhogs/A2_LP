from django import template

register = template.Library()

def capfirst(value):
    """Removes all values of arg from the given string"""
    return value.upper()