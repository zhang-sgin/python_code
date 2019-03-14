from django.conf.urls import url, include
from crm.views import login
from crm.views import depart



urlpatterns = [
    url(r'^depart/list/', depart.depart_list, name='depart_list'),
    url(r'^depart/add/', depart.depart_add, name='depart_add'),
    url(r'^depart/edit/(\d+)/', depart.depart_edit, name='depart_edit'),
    url(r'^depart/del/(\d+)/', depart.depart_del, name='depart_del'),

    url(r'^login/$',login.login,name='login'),
    url(r'^logout/$', login.logout, name='logout'),
]
