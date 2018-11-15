'''
从“学生选课系统” 这几个字就可以看出来，我们最核心的功能其实只有 选课。
角色：
    学生、管理员
功能：
    登陆 ： 管理员和学生都可以登陆，且登陆之后可以自动区分身份
    选课 ： 学生可以自由的为自己选择课程
    创建用户 ： 选课系统是面向本校学生的，因此所有的用户都应该由管理员完成
    查看选课情况 ：每个学生可以查看自己的选课情况，而管理员应该可以查看所有学生的信息
工作流程：
    登陆 ：用户输入用户名和密码
    判断身份 ：在登陆成果的时候应该可以直接判断出用户的身份 是学生还是管理员

    学生用户 ：对于学生用户来说，登陆之后有三个功能
        1、查看所有课程
        2、选择课程
        3、查看所选课程
        4、退出程序
    管理员用户：管理员用户除了可以做一些查看功能之外，还有很多创建工作
        1、创建课程
        2、创建学生学生账号
        3、查看所有课程
        4、查看所有学生
        5、查看所有学生的选课情况
        6、退出程序
'''
import  os,time
import pickle
# login_status={'username':None,'status':False}
def login(x):
    def inner(*args,**kwargs):
        count = 1
        while count < 4:
            print('请先登录')
            username=input('请输入用户名：').strip()
            password=input('请输入密码：').strip()
            with open('registry.txt',encoding='utf8')as f_registry:
                for i in f_registry:
                    login_line = i.strip().split(' ')
                    if username == login_line[0] and password == login_line[1]:
                        print('登录成功！')
                        return {'user':username,'identify':True}
                        # continue
                else:
                    print('用户名或密码错误，请重新输入，您还有{}次机会'.format(3 - count))
                    count += 1
    return inner
# print(login())

def list_class(x):
    def inner(*args,**kwargs):
        with open('class.txt', encoding='utf-8')as read_class:  # 列出所有课程
            print('当前所有课程：')
            for (num, value) in enumerate(read_class):
                print(num, value, end='')
    return inner

class Person:
    def __init__(self, name):
        self.name = name

class admin(Person):
    def a_create_class(self):
        ad_create_class=input('请输入需要创建的课程：')
        with open('class.txt',encoding='utf-8',mode='a') as create_class:
            create_class.write(ad_create_class+'\n')
        print('%s创建成功'%(ad_create_class))


    def a_create_account(self):
        register_user_name = input('请您输入需要注册的学生用户名：')
        register_password = input('请输入您需要注册的学生密码：')
        with open('registry.txt', encoding='utf-8', mode='r+')as f_register:
            for line in f_register:
                user_info = line.split(' ')
                if register_user_name in user_info:
                    print('用户已存在,请重新输入')
                    # continue
            else:
                f_register.write(register_user_name + ' ' + register_password +' '+'member' '\n')
                print('{}用户注册成功'.format(register_user_name))
        return

    # @list_class
    def a_list_class(self):
        pass

        def a_list_stu(self):
            with open('registry.txt',encoding='utf-8')as list_stu: #列出所有学生
                for i in list_stu:
                    print(i.strip().split()[0])
            return

        def a_list_all_stu_class(self):
            pass

        def a_quit(self):
            print('再见')
            quit()



class student(Person):
    s_choose_class=[]
    def list_all_class(self):
        print('当前所有课程：')
        with open('class.txt',encoding='utf-8')as read_class:
            for (num,value) in enumerate(read_class):
                print(num,value,end='')
        return

    def choose_class(self):
        # with open('class.txt',encoding='utf-8')as read_class:
        #     choose=print('请选择需要学习的课程：')
        #     for (num,value) in enumerate(read_class):
        #         print(num,value,end='')
        with open('class.txt',encoding='utf-8')as read_class:
            for i in read_class:
                print(i.strip())
        choose=input('请选择需要学习的课程：')
        with open('registry.txt',encoding='utf-8',mode='w') as add_class:
            for i2 in add_class:
                add_class.write(i2 + choose)
                print(i2)


    def s_list_stu_class(self):
        pass

    def stu_quit(self):
        print('再见')
        quit()


# p1=admin.a_create_class(0)
p1=student.choose_class(0)
