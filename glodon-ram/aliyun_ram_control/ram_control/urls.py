"""aliyun_ram_control URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from ram_control.views import ram

urlpatterns = [
    url(r'^aliyunuser/list', ram.aliyun_user_list, name='aliyun_user_list'),
    # url(r'^aliyunuser/add', ram.aliyun_user_add, name='aliyun_user_add'),


    url(r'^ramuser/list', ram.ram_user_list, name='ram_user_list'),
    url(r'^ramuser/add', ram.ram_user_add, name='ram_user_add'),
]