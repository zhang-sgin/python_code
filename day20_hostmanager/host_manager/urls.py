from django.conf.urls import url
from host_manager.views import host
from host_manager.views import bus

urlpatterns = [
    url(r'^list/', host.host_list, name='host_list'),
    url(r'^add/', host.host_change, name='host_add'),
    url(r'^edit/(\d+)/', host.host_change, name='host_edit'),

    url(r'^bus_list/', bus.bus_list, name='bus_list'),
    url(r'^bus_add/', bus.bus_change, name='bus_add'),
    url(r'^bus_edit/(\d+)/', bus.bus_change, name='bus_edit'),
]
