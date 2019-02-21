from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect,reverse
from user import models as user_models
from host import models
from django.views import View

def list_host(request):
    all_host = user_models.Host.objects.all()
    return render(request, 'list_host.html', {'all_host': all_host})


class add_host(View):
    def get(self, request):
        all_host = user_models.Host.objects.all()
        return render(request, 'add_host.html', {'all_host': all_host})

    def post(self, request):
        name = request.POST.get('hostname')
        pwd = request.POST.get('hostpwd')
        service_id = request.POST.get('pub')

        user_models.Host.objects.create(host_name=name,host_pwd=pwd,service_id=service_id)
        return redirect(reverse('list_host'))

def edit_host(request):
    return HttpResponse('<h1>edit_host</h1>')

def del_host(request):
    return HttpResponse('<h1>del_host</h1>')