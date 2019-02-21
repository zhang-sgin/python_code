from django.db import models

# Create your models here.
class User(models.Model):  # 用户表
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)  # varchar(32)
    pwd = models.CharField(max_length=32)  # varchar(32)

    def __str__(self):
        return '< 用户-{} - {} >'.format(self.pid,self.name)

class Service(models.Model):
    pid = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=32)
    user = models.ForeignKey('User',on_delete=models.CASCADE)


class Host(models.Model):
    host_name = models.CharField(max_length=32)
    host_pwd = models.CharField(max_length=32)
    service = models.ForeignKey('Service',on_delete=models.CASCADE)

class SystemUser(models.Model):
    name = models.CharField(max_length=32)  # varchar(32)
    pwd = models.CharField(max_length=32)  # varchar(32)