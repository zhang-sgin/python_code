from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
import re
from django.conf import settings


class RbacMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        
        # request.current_id = None
        setattr(request,settings.MENU,None)
        # request.breadcrumb_list = [{'url': '/crm/index/', 'title': '首页'}]
        
        # setattr(request, settings.BREADCRUMB, [{'url': '/crm/index/', 'title': '首页'}])
        setattr(request, settings.BREADCRUMB, [{'url': '/hosts/list/', 'title': '首页'}])

        # 获取当前访问的URL
        url = request.path_info
        
        # 白名单的校验
        for i in settings.VALID_LIST:
            if re.match(i, url):
                return
        
        # 获取登录状态
        is_login = request.session['is_login']
        if not is_login:
            return HttpResponse('未登录')
        
        # 已登录 校验不需要校验的地址
        for i in settings.NO_PERMISSION_LIST:
            if re.match(i, url):
                return
        
        # 获取到权限信息
        permission_dict = request.session[settings.PERMISSION_SESSION_KEY]
        print('获取权限信息')
        print(permission_dict)
        
        # 权限的校验
        for i in permission_dict.values():
            if re.match('^{}$'.format(i['url']), url):
                # 获取到二级菜单的id
                pid = i.get('pid')
                id = i.get('id')
                pname = i.get('pname')
                breadcrumb_list = getattr(request, settings.BREADCRUMB)

                if pid:
                    # 访问的是子权限  记录父权限的id
                    # request.current_id = pid
                    setattr(request, settings.MENU, pid)
                    # 添加父权限的信息
                    breadcrumb_list.append({'url': permission_dict[pname]['url'], 'title': permission_dict[pname]['title']})
                    # request.breadcrumb_list.append(
                    #     {'url': permission_dict[pname]['url'], 'title': permission_dict[pname]['title']})
                    
                
                else:
                    # 访问的是二级菜单  记录自己的id
                    # request.current_id = id
                    setattr(request, settings.MENU, id)
                breadcrumb_list.append({'url': i['url'], 'title': i['title']})
                # request.breadcrumb_list.append({'url': i['url'], 'title': i['title']})
                return
        
        # 拒绝访问
        return HttpResponse('没有访问权限')
