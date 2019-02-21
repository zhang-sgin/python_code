from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from user import models
# Create your views here.

def list_service(request):
    # return HttpResponse('<h1>zhangz-l</h1>')
    all_services = models.Service.objects.all()  # QuerySet  对象列表
    return render(request, 'list_service.html', {'all_services': all_services,'name': 'base.html'})


def add_service(request):
    return HttpResponse('<h1>add_service</h1>')

def edit_service(request):
    return HttpResponse('<h1>edit_service</h1>')

def del_service(request):
    return HttpResponse('<h1>del_service</h1>')