from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect,render,reverse
from functools import wraps

def check(func):
    def inner(request, *args, **kwargs):
        next_url = request.get_full_path()
        if request.session.get("user"):
            return func(request, *args, **kwargs)
        else:
            return redirect("/login/?next={}".format(next_url))
    return inner