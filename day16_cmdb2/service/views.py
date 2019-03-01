from django.shortcuts import render, reverse
from django.shortcuts import render, HttpResponse, redirect,render_to_response
from user import models as user_models
from service import models
from django.views import View


# Create your views here.

def list_service(request):
    all_services = user_models.Service.objects.all()  # QuerySet  对象列表
    return render(request, 'list_service.html', {'all_services': all_services, 'name': 'base.html'})


class add_service(View):
    def get(self, request):
        all_services = user_models.Service.objects.all()
        return render(request, 'add_service.html', {'all_services': all_services})

    def post(self, request):
        service_name = request.POST.get('service_name')
        user_models.Service.objects.create(service_name=service_name)
        return redirect(reverse('list_service'))


class edit_service(View):
    def get(self, request, pk):
        obj = user_models.Service.objects.filter(pk=pk).first()
        all_services = user_models.Service.objects.all()
        return render(request, 'edit_service.html', {'all_services': all_services,'obj': obj})

    def post(self, request, pk):
        edit_service = user_models.Service.objects.get(pk=pk)
        service_name = request.POST.get('service_name')
        edit_service.service_name=service_name
        edit_service.save()
        return redirect(reverse('list_service'))


def del_service(request, table, pk):
    user_models.Service.objects.get(pk=pk).delete()
    return redirect(reverse('list_service'))


def list_service_user(req):
    all_services_user = user_models.Service.objects.all()
    return render_to_response('list_user_service.html', {'all_services_user': all_services_user, 'name': 'base.html'})


# class add_service_user(View):
#     def get(self, request):
#         all_services = user_models.Service.objects.all()
#         list_user = user_models.User.objects.all()
#         return render(request, 'add_service_user.html', {'all_services': all_services, 'list_user': list_user})
#
#     def post(self, request):
#         service_id = request.POST.get('service_id')
#         user_id = request.POST.get('user_id')
#
#         user_models.User_Services.objects.create(service_id_id=service_id, user_id_id=user_id)
#         return redirect(reverse('list_service_user'))


class edit_service_user(View):
    def get(self, request, pk):
        all_services = user_models.Service.objects.all()
        list_user = user_models.User.objects.all()
        return render(request, 'edit_user_service.html', {'all_services': all_services, 'list_user': list_user})

    def post(self, request, pk):
        edit_service_user = user_models.Service.objects.get(pk=pk)
        list_user = user_models.User.objects.all()

        user_id = request.POST.getlist('user_id')
        for i in request:
            print(user_id)

        edit_service_user.user_id.set(user_id)
        edit_service_user.save()

        return redirect(reverse('list_service_user'))


# def del_service_user(request, table, pk):
#     user_obj = user_models.Service.objects.get(pk=pk)
#     user_obj.user_id.remove(pk)
#     return redirect(reverse('list_service_user'))

#
#
# class add_service_user(View):
#     def get(self, request):
#         all_services = user_models.Service.objects.all()
#         list_user = user_models.User.objects.all()
#         return render(request, 'add_service_user.html', {'all_services': all_services, 'list_user': list_user})
#
#     def post(self, request):
#         service_id = request.POST.get('service_id')
#         user_id = request.POST.get('user_id')
#
#         user_models.User_Services.objects.create(service_id_id=service_id, user_id_id=user_id)
#         return redirect(reverse('list_service_user'))
#
#
# class edit_service_user(View):
#     def get(self, request, pk):
#         all_services = user_models.Service.objects.all()
#         list_user = user_models.User.objects.all()
#         return render(request, 'add_service_user.html', {'all_services': all_services, 'list_user': list_user})
#
#     def post(self, request, pk):
#         edit_service_user = user_models.User_Services.objects.get(pk=pk)
#         print(edit_service)
#         service_id = request.POST.get('service_id')
#         user_id = request.POST.get('user_id')
#         print(service_id, user_id)
#         edit_service_user.service_id_id = service_id
#         edit_service_user.user_id_id = user_id
#         edit_service_user.save()
#         return redirect(reverse('list_service_user'))
#
#
# def del_service_user(request, table, pk):
#     user_models.User_Services.objects.get(pk=pk).delete()
#     return redirect(reverse('list_service_user'))