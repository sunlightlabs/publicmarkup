from django import template
from django.conf import settings
from publicmarkup.legislation.models import Resource

register = template.Library()

@register.simple_tag
def media_url():
    return settings.MEDIA_URL
    
@register.simple_tag
def resource(name):
    try:
        resource = Resource.objects.get(name=name)
        return resource.value
    except Resource.DoesNotExist:
        return ""
    
@register.filter
def reverse(value, limit=None):
    if value:
        max_index = len(value) - 1
        if not limit:
            limit = max_index
        offset = max_index - limit
        if offset < 0:
            offset = 0
        return reversed(value[offset:limit + offset])