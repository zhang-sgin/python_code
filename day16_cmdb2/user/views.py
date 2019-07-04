# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect,reverse
from django.contrib.auth import authenticate,login,logout
from django.views import View
from user import models

def check(func):
    def inner(request, *args, **kwargs):
        next_url = request.get_full_path()
        if request.session.get("user"):
            return func(request, *args, **kwargs)
        else:
            return redirect("/login/?next={}".format(next_url))
    return inner

def login(request):
    err_msg = ''
    if request.method == 'POST':
        login_info = request.POST
        user = login_info.get('user')
        password = login_info.get('pwd')
        if models.SystemUser.objects.filter(name=user, pwd=password):
            request.session["user"] = user
            next_url = request.GET.get("next")
            if next_url:
                return redirect(next_url)
            else:
                print('登陆成功')
                return redirect(reverse('list_user'))
    else:
        err_msg = '用户名或密码错误'
    return render(request,'login.html',{'err_msg':err_msg})


# 缺少注册功能以及注册页面，注册按钮
# class Register_User(View):
#     pass


def logout(request):
    ret = redirect("/login/")
    # 删除当前的会话数据并删除会话的Cookie。
    request.session.flush()
    return ret

@check
def list_user(request):
    all_user = models.User.objects.all()
    print(all_user,type(all_user))
    return render(request, 'list_user.html', {'all_user': all_user,'name': 'base.html'})

@check
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

@check
def del_user(request, table, pk):
    models.User.objects.get(pk=pk).delete()
    return redirect(reverse('list_user'))

@check
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