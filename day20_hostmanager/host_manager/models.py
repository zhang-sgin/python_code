from django.db import models
from rbac.models import  RbacUser

# Create your models here.

class BusinessUnit(models.Model):
    name = models.CharField(max_length=32,verbose_name='产品名称')
    level = models.CharField(max_length=32,verbose_name='服务级别')
    owner = models.CharField(max_length=32,verbose_name='负责人')

    def __str__(self):
        return self.name


class Host(models.Model):
    name = models.CharField(max_length=32, verbose_name='主机名')
    ip = models.CharField('ip地址', max_length=32, )
    bus = models.ForeignKey('BusinessUnit', on_delete=models.CASCADE, blank=True, null=True, verbose_name='业务线')


class User(RbacUser,models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)