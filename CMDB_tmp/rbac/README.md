权限组件的应用
	1. 拷贝rbac APP到新的项目中，并且要注册
	2. 数据迁移
		注意！！！: 删除rbac下的migrations下的除了__init__.py 以外的所有的py文件
		
		用户管理：
			from rbac.models import  RbacUser
			
			class User(RbacUser,models.Model):
				name = models.CharField(max_length=32)
				password = models.CharField(max_length=32)
			
		执行迁移的命令
	3. 使用admin管理权限信息
	
		创建超级用户
	
		注意： 使用原有项目的user表
		from django.contrib import admin
		from rbac import models
		from host.models import User

		# Register your models here.

		class PermissionAdmin(admin.ModelAdmin):
			list_display = ['title', 'url', 'name', 'menu']
			list_editable = ['url', 'name', 'menu']


		admin.site.register(models.Permission, PermissionAdmin)
		admin.site.register(models.Role)
		admin.site.register(models.Menu)
		admin.site.register(User)
		
		1. 权限信息的录入
			url不带 ^ $ 
			所有的url要有别名  namespace:name
		2. 菜单的管理
			录入菜单的信息
			分配二级菜单给一级菜单
			分配子权限给父权限
		3. 角色的管理
			创建角色
			给角色分配权限
		4. 用户管理
			创建用户
			给用户分配角色
			
	4. 权限控制
	
		1. 在settings配置权限的相关信息
			# ##########  权限的配置 ############
			# 白名单
			VALID_LIST = [
				'^/crm/login/$',
				'^/reg/$',
				'/admin.*',
				'/test/',
			]

			NO_PERMISSION_LIST = [
				'^/crm/index/$',

			]

			PERMISSION_SESSION_KEY = 'permissions'
			MENU_SESSION_KEY = 'menu'

						
			
		2. 登录后权限信息的初始化
			from rbac.service.permission import init_permission 
			# 登录成功后权限信息的初始化
			init_permission(request, obj)
		
		
		3. 应用上权限校验的中间件
		
	5. 动态生成菜单
		
		在母版中
		<div class="menu-body">
            {% load rbac %}
            {% menu request %}
        </div>
		
		应用上css和js样式
		    <link rel="stylesheet" href="{% static 'css/menu.css' %} "/>
			<script src="{% static 'js/menu.js' %} "></script>
			
	6. 路径导航
		   {% breadcrumb request %}
		   
		   
	7. 权限控制到按钮级别
	
	
		{% if request|has_permission:'host_edit' or request|has_permission:'host_del' %}

			<td>
				{% if request|has_permission:'host_edit' %}
					<a href="{% reverse_url request 'host_edit' host.pk %}"
					   class="btn btn-sm btn-primary">编辑</a>
				{% endif %}
			
				{% if request|has_permission:'host_del' %}
					<a href="" class="btn btn-sm btn-danger">删除</a>
				{% endif %}

			</td>
		{% endif %}