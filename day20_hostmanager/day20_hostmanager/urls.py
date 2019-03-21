"""day20_hostmanager URL Configuration

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
from host_manager.views import host

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login/', host.login, name='login'),
    url(r'^logout/',host.logout,name='logout'),
    # url(r'^crm/',host.index,name='logout'),

    url(r'^hosts/', include('host_manager.urls')),
    url(r'^bus/', include('host_manager.urls')),

]

