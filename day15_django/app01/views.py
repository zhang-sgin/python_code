from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from app01 import models

# Create your views here.
def index(request):
    return HttpResponse('<h1>zhangz-l</h1>')

def login(request):
    print(request)
    err_msg = ''
    if request.method == 'POST':
        login_info = request.POST
        user = login_info.get('user')
        password = login_info.get('pwd')
        print(models.User.objects.filter(name=user, pwd=password))
        if models.User.objects.filter(name=user, pwd=password):
            print('登陆成功')
            # return redirect('/dashboard/')
            # return redirect("http://www.sina.com")
            return render(request, 'starter.html')
        else:
            err_msg = '用户名或密码错误'
    return render(request,'login.html',{'err_msg':err_msg})
    # return render(request,'AdminLTE-2.4.5/starter.html',{'err_msg':err_msg})


def list_user(request):
    all_user = models.Systemuser.objects.all()  # QuerySet  对象列表
    return render(request, 'list_user.html', {'all_user': all_user})

def add_user(request):
    err_msg = ''
    # 处理POST请求
    if request.method == 'POST':
        # 获取提交的数据
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        if not name:
            err_msg = '不能为空'

        if  models.Systemuser.objects.filter(name=name):
            err_msg = '数据已存在'
        else:
            # 去数据库创建数据
            models.Systemuser.objects.create(name=name,password=pwd)
            return redirect('/list_user/')

    # 返回一个页面
    return render(request, 'add_user.html', {'err_msg': err_msg})

def del_user(request):
    # 获取要删除对象的ID
    pk = request.GET.get('pk')
    if models.Systemuser.objects.filter(pk=pk):
        # 去数据库进行删除
        models.Systemuser.objects.get(pk=pk).delete()  # get  查不到或者查到多个 都会报错
        # 跳转到展示页面
        return redirect('/list_user/')
    return HttpResponse('数据不存在')


def edit_user(request):
    # 获取要编辑对象的ID
    pk = request.GET.get('pk')
    obj = models.Systemuser.objects.get(pk=pk)

    err_msg = ''

    if request.method == 'POST':
        # 获取提交的名字
        new_name = request.POST.get('new_name')
        new_pwd = request.POST.get('new_pwd')

        if not new_name:
            err_msg = '不能为空'

        obj_list = models.Systemuser.objects.filter(name=new_name)

        if obj_list:
            err_msg = '数据已存在'

        if new_name and not obj_list:
            # 名字不为空且数据库不存在数据
            # obj = models.Systemuser.objects.get
            obj.name = new_name
            obj.password = new_pwd
            obj.save()

            # 跳转到展示页面
            return redirect('/list_user/')

    return render(request, 'edit_user.html', {'obj': obj, 'err_msg': err_msg})