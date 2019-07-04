from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect, reverse
from user import models as user_models
from host import models
from django.views import View
from user.views import check
from django.utils.decorators import method_decorator

@check
def list_host(request):
    all_host = user_models.Host.objects.all()
    return render(request, 'list_host.html', {'all_host': all_host})

@method_decorator(check, name='post')
class add_host(View):
    def get(self, request):
        all_host = user_models.Host.objects.all()
        list_user = user_models.User.objects.all()
        return render(request, 'add_host.html', {'all_host': all_host,'list_user': list_user})

    def post(self, request):
        name = request.POST.get('hostname')
        pwd = request.POST.get('hostpwd')
        service_id = request.POST.get('pub')

        user_models.Host.objects.create(host_name=name, host_pwd=pwd, service_id=service_id)
        return redirect(reverse('list_host'))

@method_decorator(check, name='post')
class edit_host(View):
    def get(self, request, pk):
        edit_host = user_models.Host.objects.get(pk=pk)

        # list_user = user_models.User.objects.all()
        list_service = user_models.Service.objects.all()
        return render(request, 'edit_host.html', {'edit_host': edit_host, 'list_user': list_service})


    def post(self, request, pk):
        edit_host = user_models.Host.objects.get(pk=pk)
        new_name = request.POST.get('new_name')
        new_pwd = request.POST.get('new_pwd')
        pub = request.POST.get('pub')

        print(new_name,new_pwd,pub)

        edit_host.host_name = new_name
        edit_host.host_pwd = new_pwd
        edit_host.service_id = pub
        edit_host.save()

        return redirect(reverse('list_host'))

@check
def del_host(request, table, pk):
    user_models.Host.objects.get(pk=pk).delete()
    return redirect(reverse('list_host'))