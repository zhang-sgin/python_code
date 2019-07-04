from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect,reverse
from django.contrib.auth import authenticate,login,logout
from django.views import View
from crm import models

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
                return redirect(reverse('depart_list'))
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