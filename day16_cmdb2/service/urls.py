"""day16_cmdb2 URL Configuration

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
from service import views

urlpatterns = [
    # url(r'^list_service/$', views.list_service, name='list_service'),
    # url(r'^add_service/$', views.add_service, name='add_service'),
    # url(r'^edit_service/$', views.edit_service, name='edit_service'),
    # url(r'^del_service/$', views.del_service, name='del_service'),

    url(r'^list_service/$', views.list_service, name='list_service'),
    url(r'^add_service/$', views.add_service.as_view(), name='add_service'),
    url(r'^edit_service/(\d+)/$', views.edit_service.as_view(), name='edit_service'),
    url(r'^del_(service|user)/(\d+)/$', views.del_service, name='del_service'),

    # url(r'^list_service_user/$', views.list_service_user, name='list_service_user'),
    # url(r'^add_service_user/$', views.add_service_user, name='add_service_user'),
    # url(r'^edit_service_user/$', views.edit_service_user, name='edit_service_user'),
    # url(r'^del_service_user/$', views.del_service_user, name='del_service_user'),

    url(r'^list_service_user/$', views.list_service_user, name='list_service_user'),
    # url(r'^add_service_user/$', views.add_service_user.as_view(), name='add_service_user'),
    url(r'^edit_service_user/(\d+)/$', views.edit_service_user.as_view(), name='edit_service_user'),
    # url(r'^del_service_(host|user)/(\d+)/$', views.del_service_user, name='del_service_user'),
]