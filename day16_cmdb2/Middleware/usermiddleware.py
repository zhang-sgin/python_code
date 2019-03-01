from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect,render,reverse
from user import models


class Login(MiddlewareMixin):
    def process_request(self, request):
        err_msg = ''
        if request.method == 'POST':
            login_info = request.POST
            user = login_info.get('user')
            password = login_info.get('pwd')
            if models.SystemUser.objects.filter(name=user, pwd=password):
                print('登陆成功')
                return redirect(reverse('list_user'))
            else:
                err_msg = '用户名或密码错误'
        return render(request, 'login.html', {'err_msg': err_msg})
