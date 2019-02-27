from django.db import models

# Create your models here.
class User(models.Model):  # 用户表
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)  # varchar(32)
    pwd = models.CharField(max_length=32)  # varchar(32)

    def __str__(self):
        # return '< 用户-{} - {} >'.format(self.pid,self.name)
        return "用户表 - ID:{} - Username:{} - Password{}".format(self.pk,self.name,self.pwd)

class Service(models.Model):    #业务线表
    pid = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=32)
    user_id = models.ManyToManyField('User')

    def __str__(self):
        return "业务线表 - ID:{} - Service_name:{} - User_ID:{}".format(self.pk,self.service_name,self.user_id)

# class User_Services(models.Model):
#     pid = models.AutoField(primary_key=True)
#     service_id = models.ManyToManyField('service')
#     user_id = models.ManyToManyField('user')
#
#     class Meta:
#         db_table = "User_Services_day17"
#     def __str__(self):
#         return "业务线与负责人关系表 - ID:{} - Service_ID:{} - User_ID:{}".format(self.pk,self.service_id,self.user_id)

# class User_Services(models.Model):  #用户和业务线关联表
#     pid = models.AutoField(primary_key=True)
#     service_id = models.ForeignKey('Service',on_delete=models.CASCADE)
#     user_id = models.ForeignKey('User',on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = "User_Services_day17"
#
#     def __str__(self):
#         return "业务线与负责人关系表 - ID:{} - Service_ID:{} - User_ID:{}".format(self.pk,self.service_id,self.user_id)


class Host(models.Model):
    host_name = models.CharField(max_length=32)
    host_pwd = models.CharField(max_length=32)
    service = models.ForeignKey('Service',on_delete=models.CASCADE)

    def __str__(self):
        return "主机表 - ID:{} - Host_name:{} - Host_pwd:{} - service:{} ".format(self.pk,self.host_name,self.host_pwd,self.service)

class SystemUser(models.Model):
    name = models.CharField(max_length=32)  # varchar(32)
    pwd = models.CharField(max_length=32)  # varchar(32)

    def __str__(self):
        return "系统用户 - ID:{} - SystemUser:{} - SystemUser_Pwd:{}".format(self.pk,self.name,self.pwd)

