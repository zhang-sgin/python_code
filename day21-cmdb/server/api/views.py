from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import json

@csrf_exempt
def asset(request):
    if request.method == 'GET':
        host_list = ['127.0.0.1','127.0.0.2']
        return JsonResponse(host_list,safe=False)
    else:
        data = json.loads(request.body.decode('gbk'))
        print(data)
        return HttpResponse('ok')

class Asset(APIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request):
        host_list = ['127.0.0.1', '127.0.0.2']
        return  JsonResponse(host_list,safe=False)

    def post(self,request):
        data = json.loads(request.body.decode('gbk'))
        print(data)
        return HttpResponse('ok')



