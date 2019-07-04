from django.shortcuts import HttpResponse, render, redirect, reverse
from crm import models
from django import forms
from django.http import JsonResponse
from crm.views.login import check


@check
def depart_list(request):
    all_depart = models.Depart.objects.all()
    return render(request, 'depart_list.html', {'all_depart': all_depart, 'name': 'base.html'})


class DepartForm(forms.ModelForm):
    class Meta:
        model = models.Depart
        fields = "__all__"

        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'form-control'})
        }

        error_messages = {
            'name': {
                'required': '不能为空'
            }
        }

        labels = {
            # 'name':'部门名称'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

@check
def depart_add(request):
    form_obj = DepartForm()
    if request.method == 'POST':
        form_obj = DepartForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('depart_list'))

    return render(request, 'depart_add.html', {'form_obj': form_obj,'name': 'base.html'})

@check
def depart_edit(request, edit_id):
    obj = models.Depart.objects.filter(pk=edit_id).first()
    form_obj = DepartForm(instance=obj)

    if request.method == 'POST':
        form_obj = DepartForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('depart_list'))

    return render(request, 'depart_edit.html', {'form_obj': form_obj,'name': 'base.html'})

@check
def depart_del(request, del_id):
    ret = {'status': 0, 'msg': None}
    try:
        pass
    except Exception as e:
        ret['status'] = 1
        ret['msg'] = str(e)
    return JsonResponse(ret)
