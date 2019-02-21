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
from user import views
from host import views as hostview

urlpatterns = [
    url(r'^list_host/$',hostview.list_host,name='list_host'),
    url(r'^add_host/$',hostview.add_host,name='add_host'),
    url(r'^edit_host/$',hostview.edit_host,name='edit_host'),
    url(r'^del_host/$',hostview.del_host,name='del_host'),
]



# urlpatterns = [
#     url(r'^login/$',views.login,name='login'),
#     url(r'^list_user/$',views.list_user,name='list_user'),
#     url(r'^add_user/$',views.add_user,name='add_user'),
#
#     url(r'^edit_user/$',views.edit_user,name='edit_user'),
#     url(r'^edit_(?P<name>list_user)/(?P<pk>\d+)/$', views.edit_user, name='edit_user'),
#
#     url(r'^del_(host|user)/(\d+)/$', views.del_user, name='del_user'),
#
# ]