from django.template import Library
register = Library()
from django.conf import settings
from collections import OrderedDict


@register.inclusion_tag('menu.html')
def menu(request):
    # url = request.path_info
    menus_dict = request.session[settings.MENU_SESSION_KEY]
    """
    {1:
         {'title': '信息管理',
          'icon': 'fa-ravelry',
          'weight': 100,
          'children':
              [{'title': '部门列表', 'url': '/crm/depart/list/'},
               {'title': '班级列表', 'url': '/crm/class/list/'}]
          },
     }
    
    """
    ordered_dict = OrderedDict()
    
    # for key in [2,1]
    for key in sorted(menus_dict, key=lambda x: menus_dict[x]['weight'], reverse=True):
        #  menus_dict[2]  一级菜单的字典
        i = ordered_dict[key] = menus_dict[key]
        
        i['class'] = 'hide'
        for child in i['children']:
            #  child 二级菜单  id
            # if child['id'] == request.current_id:
            if child['id'] == getattr(request, settings.MENU):
                child['class'] = 'active'
                i['class'] = ''
    
    return {'menus_list': ordered_dict.values()}


@register.inclusion_tag('breadcrumb.html')
def breadcrumb(request):
    # breadcrumb_list = request.breadcrumb_list
    breadcrumb_list = getattr(request, settings.BREADCRUMB)
    return {'breadcrumb_list': breadcrumb_list}


@register.filter
def has_permission(request, name):
    if name in request.session[settings.PERMISSION_SESSION_KEY]:
        return True
