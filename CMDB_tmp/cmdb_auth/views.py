from django.shortcuts import render
from django import forms
from django.shortcuts import render, redirect, reverse
from utils.pagination import Pagination
from utils.reverse_url import reverse_url
from cmdb_auth import models
from rbac.service.permission import init_permission


def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        obj = models.User.objects.filter(name=user, password=pwd).first()
        if not obj:
            # 认证失败
            return render(request, 'login.html', {"error": '用户名或密码错误'})

        # 登录成功后权限信息的初始化
        init_permission(request, obj)

        # 跳转
        return redirect(reverse('host_list'))

    return render(request, 'login.html')


def logout(request):
    ret = redirect("/login/")
    request.session.flush()
    return ret
