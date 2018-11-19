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
import  os,time,json
# class admin:
#     def __init__(self,name):
#         self.name = name
#
#     def a_create_class(self):
#         print('1.创建课程')
#         ad_create_class=input('请输入需要创建的课程：')
#         with open('class.txt',encoding='utf-8',mode='a') as create_class:
#             create_class.write(ad_create_class+'\n')
#         print('%s创建成功'%(ad_create_class))
#
#
#     def a_create_account(self):
#         print('2.注册学员')
#         register_user_name = input('请您输入需要注册的学生用户名：')
#         register_password = input('请输入您需要注册的学生密码：')
#         with open('registry.txt', encoding='utf-8', mode='r+')as f_register:
#             for line in f_register:
#                 user_info = line.split(' ')
#                 if register_user_name in user_info:
#                     print('用户已存在,请重新输入')
#                     # continue
#             else:
#                 f_register.write(register_user_name + ' ' + register_password +' ' + 'member' '\n')
#                 print('{}用户注册成功'.format(register_user_name))
#         return
#
#     def a_list_class(self):
#         print('3.查看当前所有课程')
#         with open('class.txt',encoding='utf-8')as read_class:
#             for (num,value) in enumerate(read_class):
#               print(num,value,end='')
#             return
#
#     def a_list_stu(self):
#         print('4.查看所有学生')
#         with open('registry.txt',encoding='utf-8')as list_stu: #列出所有学生
#             for i in list_stu:
#                 print(i.strip().split()[0])
#         return
#
#     def a_list_all_stu_class(self):
#         print('5.查看所有学生的选课情况')
#         with open('choose_class.txt',encoding='utf-8') as read_all_class:
#             for i in read_all_class:
#                 print(i.strip())
#
#     def a_quit(self):
#         print('6.退出')
#         print('再见')
#         quit()
#
#
#
# class student:
#     s_choose_class=[]
#     def __init__(self,name):
#         self.name = name
#
#     def list_all_class(self):
#         print('1.查看当前所有课程')
#         with open('class.txt',encoding='utf-8')as read_class:
#             for (num,value) in enumerate(read_class):
#                 print(num,value,end='')
#         return
#
#     def choose_class(self):
#         print('2.选择课程')
#         with open('class.txt',encoding='utf-8')as read_class:
#             for (num,value) in enumerate(read_class):
#                 print(num+1,value,end='')
#         # with open('class.txt',encoding='utf-8')as read_class:
#         #     for i in read_class:
#         #         print(i.strip())
#         choose=input('请选择需要学习的课程：')
#         with open('choose_class.txt',encoding='utf-8',mode='r+') as add_class:
#             for line in add_class:
#                 choose_line = line.split(' ')
#                 if self.name and choose in  choose_line:
#                     print('课程已选，请重新输入')
#                     # continue
#             else:
#                 add_class.write(self.name + ' ' + choose +'\n')
#                 print('亲爱的%s,您已选择%s课程'%(self.name,choose))
#
#     def s_list_stu_class(self):
#         print('3.查看当前用户的选课情况')
#         with open('choose_class.txt',encoding='utf-8') as read_class:
#             for i in read_class:
#                 print(i.strip())
#
#
#     def stu_quit(self):
#         print('4.退出')
#         print('再见')
#         quit()



# def login():
#     print('欢迎来到选课系统！')
#     count = 1
#     while count < 4:
#         print('请先登录')
#         username=input('请输入用户名：').strip()
#         password=input('请输入密码：').strip()
#         role=input('请输入身份(admin/member):')
#         with open('registry.txt',encoding='utf8')as f_registry:
#             for i in f_registry:
#                 login_line = i.strip().split(' ')
#                 print(login_line)
#                 if username == login_line[0] and password == login_line[1]:  #z 123 member zz 234 admin
#                     print('%s %s登录成功！'%(login_line[2],username))
#
#             else:
#                 print('用户名或密码错误，请重新输入，您还有{}次机会'.format(3 - count))
#                 count += 1


class student:
    def __init__(self, name):
        self.name = name
    
    def list_class(self):
        with open("new_class", 'r', encoding="utf8") as f_read_class:
            tmp = {}
            for index, i in enumerate(f_read_class.read().split("|"), 1):
                print(index, i)
                tmp[str(index)] = i
            print(tmp)
            return tmp
    
    def choose_class(self):
        tmp = self.list_class()
        stu_choose_class = input("请选择你要选的课程的序号:")
        if stu_choose_class in tmp:
            with open("user_class", 'r', encoding="utf8") as f:
                user_class = json.load(f)
                print(user_class,type(user_class))
                if user_class.get(self.name):
                    user_class.get(self.name).append(tmp[stu_choose_class])
                else:
                    user_class.setdefault(self.name, [tmp[stu_choose_class]])
            
            with open("user_class", 'w', encoding="utf8") as f:
                json.dump(user_class, f, ensure_ascii=False)
    
    def list_stu_class(self):
        with open("user_class", 'r', encoding="utf8") as f:
            user_class = json.load(f)
            stu_list = user_class.get(self.name)
            stu_list = list(set(stu_list))
            print(stu_list)
    
    def exit(self):
        exit()
    
    def show(self):
        gongneng = {"查看课程": self.list_class, '选择课程': self.choose_class, "查看所选课程": self.list_stu_class, "退出": self.exit}
        while 1:
            tmp = {}
            for index, i in enumerate(gongneng, 1):
                print(index, i)
                tmp[str(index)] = gongneng[i]
            C = input("请输入你的选择:")
            if C in tmp:
                tmp[C]()

class admin:
    def __init__(self, name):
        self.name = name
     
    def a_create_class(self):
        create_class=input('请输入新增的课程：')
        with open('new_class',encoding='utf-8',mode='a')as f_create_class:
            f_create_class.write(create_class+'|')
            
    def a_create_account(self):
        register_user_name = input('请您输入需要注册的学生用户名：')
        register_password = input('请输入您需要注册的学生密码：')
        with open('new_user', encoding='utf-8', mode='r+')as f_register:
            for line in f_register:
                user_info = line.split('|')
                if register_user_name in user_info:
                    print('用户已存在,请重新输入')
                    # continue
            else:
                f_register.write(register_user_name + '|' + register_password +'|' + 'member' '\n')
                print('{}用户注册成功'.format(register_user_name))
                
    def a_list_class(self):
        print('查询所有课程')
        with open("new_class", 'r', encoding="utf8") as f_read_class:
            tmp = {}
            for index, i in enumerate(f_read_class.read().split("|"), 1):
                print(index, i)
                tmp[str(index)] = i
            return tmp
        
    def a_list_stu(self):
        print('查询所有学生')
        with open('new_user', encoding='utf-8')as f_list_stu:
            for i in f_list_stu:
                print(i.strip().split('|')[0])
                
    def a_list_stu_class(self):
        list_stu_name=input('请输入查询学生姓名：')
        with open("user_class", 'r', encoding="utf8") as f:
            user_class = json.load(f)
            stu_list = user_class.get(list_stu_name)
            stu_list = list(set(stu_list))
            print(stu_list)
            
    def admin_exit(self):
        exit()

    def show(self):
        gongneng = {"创建课程":self.a_create_class, '创建学生账号': self.a_create_account, "查看所有课程": self.a_list_class,
                    "查看所有学员": self.a_list_stu,"查看学员选课情况":self.a_list_stu_class,"退出":self.admin_exit}
        while 1:
            tmp = {}
            for index, i in enumerate(gongneng, 1):
                print(index, i)
                tmp[str(index)] = gongneng[i]
            C = input("请输入你的选择:")
            if C in tmp:
                tmp[C]()

# s = student("zz")
# s.show()
# student.choose_class(0)
# z=admin('zz')
# z.a_list_stu_class()

def login():
    print('欢迎来到选课系统！')
    count = 1
    while count < 4:
        print('请先登录')
        username=input('请输入用户名：').strip()
        password=input('请输入密码：').strip()
        with open('new_user',encoding='utf8')as f_registry:
            for i in f_registry:
                login_line = i.strip().split('|')
                if username == login_line[0] and password == login_line[1]:  #z 123 member zz 234 admin
                    if login_line[2]=='admin':
                        print('管理员%s登录成功！'%(username))
                        admin_user=admin(username)
                        admin_user.show()
                        return
                    elif login_line[2] == 'member':
                        print('学员%s登录成功！' % (username))
                        student_user=student(username)
                        student_user.show()
                        return

            else:
                print('用户名或密码错误，请重新输入，您还有{}次机会'.format(3 - count))
                count += 1
login()