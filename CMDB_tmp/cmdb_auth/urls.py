from django.conf.urls import url
from cmdb_auth import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
]