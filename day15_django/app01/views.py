from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from app01 import models

# Create your views here.
def index(request):
    return HttpResponse('<h1>zhangz-l</h1>')

def login(request):
    err_msg = ''
    if request.method == 'POST':
        login_info = request.POST
        user = login_info.get('user')
        password = login_info.get('pwd')
        print(models.User.objects.filter(name=user, pwd=password))
        if models.User.objects.filter(name=user, pwd=password):
            print('登陆成功')
            return redirect('/index/')
        else:
            err_msg = '用户名或密码错误'
    return render(request,'login.html',{'err_msg':err_msg})