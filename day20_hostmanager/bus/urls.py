from django.conf.urls import url
from bus.views import bus

urlpatterns = [
    url(r'^list/', bus.bus_list, name='bus_list'),
    url(r'^add/', bus.bus_change, name='bus_add'),
    url(r'^edit/(\d+)/', bus.bus_change, name='bus_edit'),
]
