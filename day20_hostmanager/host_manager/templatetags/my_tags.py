from django import template

register = template.Library()

from django.urls import reverse


@register.simple_tag
def reverse_url(request, url_name, *args, **kwargs):
    params = request.GET.urlencode()
    
    url = reverse(url_name, args=args, kwargs=kwargs)
    
    return "{}?{}".format(url, params)
