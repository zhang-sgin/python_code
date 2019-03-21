from django.urls import reverse


def reverse_url(request, url_name, *args, **kwargs):
    params = request.GET.urlencode()
    
    if params:
        url = '{}?{}'.format(reverse(url_name, args=args, kwargs=kwargs), params)
    else:
        url = reverse(url_name, args=args, kwargs=kwargs)
    return url
