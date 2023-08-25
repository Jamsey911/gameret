"""Imports for templatetags to calcalate subtotoal in bag"""
from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """Model to Calcalate subtotal for cart"""
    return price * quantity
