from django.conf import settings


def init_permission(request, obj, ):
    # 认证成功
    
    permission_query = obj.roles.filter(permissions__url__isnull=False).values(
        'permissions__url',
        'permissions__title',
        'permissions__name',
        'permissions__menu_id',
        'permissions__menu__title',
        'permissions__menu__icon',
        'permissions__menu__weight',
        'permissions__id',
        'permissions__parent_id',
        'permissions__parent__name',
    ).distinct()
    
    # 保存权限信息
    permission_dict = {}
    
    # 保存菜单的信息
    menu_dict = {}
    
    for i in permission_query:
        permission_dict[i['permissions__name']] = {'url': i['permissions__url'],
                                                   'id': i['permissions__id'],
                                                   'pid': i['permissions__parent_id'],
                                                   'title': i['permissions__title'],
                                                   'pname': i['permissions__parent__name'],
                                                   }
        
        menu_id = i['permissions__menu_id']
        # 不是二级菜单 再次循环
        if not menu_id:
            continue
        # 是二级菜单
        if menu_id not in menu_dict:
            # 构建一级菜单 和 二级菜单的信息（多放了二级菜单的id）
            menu_dict[menu_id] = {
                'title': i['permissions__menu__title'],
                'icon': i['permissions__menu__icon'],
                'weight': i['permissions__menu__weight'],
                'children': [
                    {'title': i['permissions__title'], 'url': i['permissions__url'], 'id': i['permissions__id']}]
            }
        else:
            # 把当前二级菜单 添加到对应一级菜单的children
            menu_dict[menu_id]['children'].append(
                {'title': i['permissions__title'], 'url': i['permissions__url'], 'id': i['permissions__id']})
    
    request.session[settings.PERMISSION_SESSION_KEY] = permission_dict
    request.session[settings.MENU_SESSION_KEY] = menu_dict
    request.session['is_login'] = True
