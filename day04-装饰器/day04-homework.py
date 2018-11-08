'''
作业：模拟博客园登录：
	1)，启动程序，首页面应该显示成如下格式：
		欢迎来到博客园首页
		1:请登录
		2:请注册
		3:文章页面
		4:日记页面
		5:评论页面
		6:收藏页面
		7:注销
		8:退出程序
	2)，用户输入选项，3~6选项必须在用户登录成功之后，才能访问成功。
	3)，用户选择登录，用户名密码从register文件中读取验证，三次机会，没成功则结束整个程序运行，
	    成功之后，可以选择访问3~6项，访问页面之前，必须要在log文件中打印日志，日志格式为-->用户:xx 在xx年xx月xx日 执行了 %s函数，
	    访问页面时，页面内容为：欢迎xx用户访问评论（文章，日记，收藏）页面
	4)，如果用户没有注册，则可以选择注册，注册成功之后，可以自动完成登录，然后进入首页选择。
	5)，注销用户是指注销用户的登录状态，使其在访问任何页面时，必须重新登录。
	6)，退出程序为结束整个程序运行。
'''

import  os,time
login_status={'username':None,'status':False}
def login(x):
    def inner(*args,**kwargs):
        if login_status['status']:
            ret = x(*args,**kwargs)
            return ret
        else:
            count = 1
            while count <4:
                print('请先登录')
                username=input('请输入用户名：').strip()
                password=input('请输入密码：').strip()
                with open('registry2.txt',encoding='utf8')as f_registry:
                    for i in f_registry:
                        login_line=i.strip().split(' ')
                        # print(login_line)
                        if username == login_line[0] and password ==login_line[1]:
                            login_status['username'] = username
                            login_status['status'] = password
                            ret=x(*args,**kwargs)
                            return ret
                    else:
                        print('用户名或密码错误，请重新输入，您还有{}次机会'.format(3 - count))
                        count += 1
    return inner


def register():
    register_user_name = input('请注册您的用户名：')
    register_password = input('请注册您的用户名密码：')
    with open('registry2.txt', encoding='utf-8',mode='r+')as f_register:
        for line in f_register:
            user_info = line.split(' ')
            if register_user_name in user_info:
                print('用户已存在')
                continue
            else:
                f_register.write(register_user_name + ' ' + register_password + '\n')
                print('{}用户注册成功'.format(register_user_name))
                login_status['username'] = register_user_name
                login_status['status'] = register_password

def timeer(x):
    def inner(*args,**kwargs):
        struct_time = time.localtime()
        time_info = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
        with open('home-log.txt',encoding='utf-8',mode='a')as f_log:
            f_log.write('%s先生在%s时，执行了%s函数\n'%(login_status['username'],time_info,x.__name__))
            ret = x(*args,**kwargs)
            return ret
    return inner

@login
@timeer
def wenzhang():
    print('欢迎%s打开文章页面'%(login_status['username']))

@login
@timeer
def riji():
    print('欢迎%s打开日记页面' % (login_status['username']))

@login
@timeer
def comment():
    print('欢迎%s打开评论页面' % (login_status['username']))

@login
@timeer
def shoucang():
    print('欢迎%s打开收藏页面' % (login_status['username']))

def zhuxiao():
    login_status['username'] = None
    login_status['status'] = False
    print('您登陆的用户已注销请重新登录')

def tuichu():
    quit()

dic = {
    1:login,
    2:register,
    3: wenzhang,
    4: riji,
    5:comment,
    6:shoucang,
    7:zhuxiao,
    8:tuichu
}

while 1:
    num = input("""欢迎来到博客园首页\n1:请登录\n2:请注册\n3:文章页面\n4:日记页面\n5:评论页面\n6:收藏页面\n7:注销\n8:退出程序\n请选择功能：""").strip()
    dic[int(num)]()

