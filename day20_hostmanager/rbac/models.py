from django.db import models


class Menu(models.Model):
    """
    菜单表 一级菜单
    """
    title = models.CharField(max_length=32)
    icon = models.CharField(max_length=32)
    weight = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title


class Permission(models.Model):
    """
    权限表
    menu_id
        权限有menu_id               ——》 当的权限是二级菜单   父权限
        权限没有menu_id有parent_id   ——》 当的权限是二级菜单下的子权限
        
    一级菜单
        二级菜单
        二级菜单
            子权限
            子权限
        

    """
    url = models.CharField('含正则的URL', max_length=128)
    title = models.CharField('标题', max_length=32, blank=True, null=True)
    name = models.CharField('URL别名', max_length=32, unique=True)  # unique=True 最后加
    menu = models.ForeignKey('Menu', blank=True, null=True)  # menu_id
    parent = models.ForeignKey('Permission', blank=True, null=True)  # parent_id
    
    def __str__(self):
        return self.title


class Role(models.Model):
    """
    角色表
    """
    name = models.CharField('角色名称', max_length=32)
    permissions = models.ManyToManyField('Permission', verbose_name='角色拥有的权限', blank=True)
    
    def __str__(self):
        return self.name


class RbacUser(models.Model):
    """
    用户表
    """
    # name = models.CharField('用户名',max_length=32)
    # password = models.CharField('密码',max_length=32)
    roles = models.ManyToManyField(Role, verbose_name='用户拥有的角色', blank=True)
    
    class Meta:
        abstract = True  # 数据库迁移时不生成表，这张表当做基类用做继承
