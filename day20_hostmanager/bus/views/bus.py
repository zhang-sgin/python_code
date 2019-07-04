from django import forms
from django.shortcuts import render, redirect, reverse
from utils.pagination import Pagination
from utils.reverse_url import reverse_url
from host_manager import models


def bus_list(request):
    all_bus = models.BusinessUnit.objects.all()
    
    page = Pagination(request.GET.get('page', '1'), all_bus.count())
    return render(request, 'bus_list.html', {'all_bus': all_bus[page.start:page.end],'page_html': page.page_html})


class BustForm(forms.ModelForm):
    class Meta:
        model = models.BusinessUnit
        fields = '__all__'  # []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


def bus_change(request, edit_id=None):
    bus_obj = models.BusinessUnit.objects.filter(pk=edit_id).first()
    
    form_bus_obj = BustForm(instance=bus_obj)
    if request.method == 'POST':
        form_bus_obj = BustForm(request.POST, instance=bus_obj)
        if form_bus_obj.is_valid():
            form_bus_obj.save()
            return redirect(reverse_url(request, 'bus_list'))
    
    title = '编辑业务线' if edit_id else '新增业务线'
    return render(request, 'form.html', {'form_obj': form_bus_obj, 'title': title})
