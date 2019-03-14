from django.db import models

class Depart(models.Model):
    name = models.CharField(max_length=32, verbose_name='部门名称')
    desc = models.TextField(blank=True, null=True, verbose_name='职责')


class SystemUser(models.Model):
    name = models.CharField(max_length=32)  # varchar(32)
    pwd = models.CharField(max_length=32)  # varchar(32)

    def __str__(self):
        return "系统用户 - ID:{} - SystemUser:{} - SystemUser_Pwd:{}".format(self.pk,self.name,self.pwd)