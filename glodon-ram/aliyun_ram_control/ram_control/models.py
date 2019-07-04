from django.db import models


class System_User(models.Model):
    name = models.CharField(max_length=32)  # varchar(32)
    pwd = models.CharField(max_length=32)  # varchar(32)

    def __str__(self):
        return "系统用户 - ID:{} - SystemUser:{} - SystemUser_Pwd:{}".format(self.pk, self.name, self.pwd)


class User(models.Model):
    name = models.CharField(max_length=32)  # varchar(32)
    pwd = models.CharField(max_length=32)  # varchar(32)

    def __str__(self):
        return "普通用户 - ID:{} - User:{} - User:{}".format(self.pk, self.name, self.pwd)


class Aliyun_User(models.Model):
    user_name = models.TextField(max_length=128, null=True, verbose_name='阿里云用户名称')
    AccessKeyID = models.TextField(max_length=128, null=True, verbose_name='阿里云用户key')
    AccessKeySecret = models.TextField(max_length=128, null=True, verbose_name='阿里云用户秘钥')

    def __str__(self):
        return self.user_name


class Aliyun_Ram_User(models.Model):
    aliyun_user_name = models.ForeignKey('Aliyun_User', on_delete=models.CASCADE, blank=True, null=True,
                                         verbose_name='阿里云用户名称')
    ram_user_name = models.CharField(max_length=128, null=True, verbose_name='RAM用户名')
    ram_display_name = models.CharField(max_length=128, null=True, verbose_name='RAM用户显示名称')
    ram_user_accesskey = models.CharField(max_length=128, null=True, verbose_name='RAM用户key')
    ram_auth = models.TextField(max_length=2048,null=True, verbose_name='RAM用户权限列表')
    ram_phone = models.CharField(max_length=128, null=True, verbose_name='RAM用户手机号')
    ram_mail = models.CharField(max_length=128, null=True, verbose_name='RAM用户邮箱')
    ram_comment = models.CharField(max_length=128, null=True, verbose_name='备注')

    def __str__(self):
        return "RAM用户 - ID:{} - ram_user_name:{} - ram_auth:{}".format(self.pk, self.ram_display_name, self.ram_auth)
