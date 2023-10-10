"""Imports for templatetags to display paginated products"""
from django import template

register = template.Library()


@register.simple_tag
def relative_url(value, field_name, urlencode=None):
    """
    Required to show the next page from the search query
    rather than the show all products query
    """
    url = '?{}={}'.format(field_name, value)
    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split(
            '=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)
    return url
