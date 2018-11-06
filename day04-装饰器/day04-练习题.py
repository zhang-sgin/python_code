'''
1、整理装饰器的形成过程，背诵装饰器的固定格式\
'''



'''
2、编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码’
'''
# def func1():
#     print('haha,func1')
# def wrapper(x):
#     def inner(*args,**kwargs):
#         print('每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码')
#         ret=x(*args,**kwargs)
#         return ret
#     return inner
# func1 = wrapper(func1)
# func1()
'''
3、编写装饰器,在每次执行被装饰函数之后打印一句’每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码’
'''
# def func1():
#     print('haha,func1')
# def wrapper(x):
#     def inner(*args,**kwargs):
#         ret=x(*args,**kwargs)
#         print('每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码')
#         return ret
#     return inner
# func1 = wrapper(func1)
# func1()

'''
4、编写装饰器,在每次执行被装饰函数之前让用户输入用户名,密码,给用户三次机会,登录成功之后,才能访问该函数.
'''
# login_status={'username':None,'status':False}
# def login(x):
#     def inner(*args,**kwargs):
#         if login_status['status']:
#             ret = x(*args,**kwargs)
#             return ret
#         else:
#             print('请先登录')
#             username=input('请输入用户名：').strip()
#             password=input('请输入密码：').strip()
#             if username == 'zz' and password =='123':
#                 login_status['username']=username
#                 login_status['status']=password
#                 ret=x(*args,**kwargs)
#                 return ret
#     return inner
# @login
# def nice():
#     print('漂亮，登录成功')
# nice()


'''
5、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,只支持单用户的账号密码,给用户三次机会），要求登录成功一次，后续的函数都无需再输入用户名和密码
'''
login_status={'username':None,'status':False}
def login(x):
    def inner(*args,**kwargs):
        if login_status['status']:
            ret = x(*args,**kwargs)
            return ret
        else:
            print('请先登录')
            username=input('请输入用户名：').strip()
            password=input('请输入密码：').strip()
            if username == 'zz' and password =='123':
                login_status['username']=username
                login_status['status']=password
                ret=x(*args,**kwargs)
                return ret
    return inner


@login
def nice():
    print('漂亮，nice打印成功')


@login
def perfect():
    print('漂亮,perfect打印成功')

dic = {
    1: nice,
    2: perfect,
}

while 1:
    print('''
    1.nice
    2.perfect
    ''')
    num = input('请输入数字：').strip()
    dic[int(num)]()

'''
6，编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,可支持多账号密码），要求登录成功一次（给三次机会），后续的函数都无需再输入用户名和密码。
'''


'''
	7，给每个函数写一个记录日志的功能，
		功能要求：每一次调用函数之前，要将函数名称，时间节点记录到log的日志中。
		所需模块：
		import time
		struct_time = time.localtime()
		print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time))
'''