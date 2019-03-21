from django import forms
from django.shortcuts import render, redirect, reverse
from utils.pagination import Pagination
from utils.reverse_url import reverse_url
from host_manager import models
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




def host_list(request):
    all_host = models.Host.objects.all()
    
    page = Pagination(request.GET.get('page', '1'), all_host.count())
    return render(request, 'host_list.html', {'all_host': all_host[page.start:page.end],'page_html': page.page_html})


class HostForm(forms.ModelForm):
    class Meta:
        model = models.Host
        fields = '__all__'  # []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


def host_change(request, edit_id=None):
    obj = models.Host.objects.filter(pk=edit_id).first()
    
    form_obj = HostForm(instance=obj)
    if request.method == 'POST':
        form_obj = HostForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse_url(request, 'host_list'))
    
    title = '编辑主机' if edit_id else '新增主机'
    return render(request, 'form.html', {'form_obj': form_obj, 'title': title})
