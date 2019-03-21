from django.conf.urls import url
from host_manager.views import host

urlpatterns = [
    url(r'^list/', host.host_list, name='host_list'),
    url(r'^add/', host.host_change, name='host_add'),
    url(r'^edit/(\d+)/', host.host_change, name='host_edit'),

]
