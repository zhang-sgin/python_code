# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect,reverse
from django.contrib.auth import authenticate,login,logout
from django.views import View
from user import models

def login(request):
    err_msg = ''
    if request.method == 'POST':
        login_info = request.POST
        user = login_info.get('user')
        password = login_info.get('pwd')
        if models.SystemUser.objects.filter(name=user, pwd=password):
            print('登陆成功')
            return redirect(reverse('list_user'))
        else:
            err_msg = '用户名或密码错误'
    return render(request,'login.html',{'err_msg':err_msg})


# class Uselogin(View):
#     def get(self, request):
#         all_host = models.User.objects.all()
#         list_user = models.User.objects.all()
#         return render(request, 'add_host.html', {'all_host': all_host,'list_user': list_user})
#
#     def post(self, request):
#         name = request.POST.get('hostname')
#         pwd = request.POST.get('hostpwd')
#         service_id = request.POST.get('pub')
#
#         models.User.objects.create(host_name=name, host_pwd=pwd, service_id=service_id)
#         return redirect(reverse('list_host'))






def list_user(request):
    all_user = models.User.objects.all()
    return render(request, 'list_user.html', {'all_user': all_user,'name': 'base.html'})

def add_user(request):
    err_msg = ''
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        print(name,pwd)
        if not name:
            err_msg = '不能为空'
        if  models.User.objects.filter(name=name):
            err_msg = '数据已存在'
        else:
            models.User.objects.create(name=name,pwd=pwd)
            return redirect(reverse('list_user'))
    return render(request, 'add_user.html', {'err_msg': err_msg})


def del_user(request, table, pk):
    models.User.objects.get(pk=pk).delete()
    return redirect(reverse('list_user'))

def edit_user(request, name, pk):
    obj = models.User.objects.filter(pk=pk).first()
    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        new_pwd = request.POST.get('new_pwd')
        obj.name = new_name
        obj.pwd = new_pwd
        obj.save()
        return redirect(reverse('list_user'))

    return render(request, 'edit_user.html', {'obj': obj})