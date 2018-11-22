'''
需求：
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
    判断身份 ：在登陆成果的时候应该可以直接判断出用户的身份 是学生、讲师还是管理员
    学生用户 ：对于学生用户来说，登陆的工作几乎不变
        1、查看所有课程
        2、选择课程
        3、查看所选课程
        4、退出程序
    管理员用户：管理员用户也可以做更多的事情

        1、创建课程
        2、创建学生学生账号
        3、查看所有课程
        4、查看所有学生
        5、查看所有学生的选课情况
        6、创建讲师
        7、为讲师指定班级
        8、创建班级
        9、为学生指定班级
        10、退出程序

    讲师用户 ：对于讲师用户来说，可以完成的功能如下
        1、查看所有课程
        2、查看所教班级
        3、查看班级中的学生
        4、退出程序
'''
import json

print(
    '''
    文件描述：
    classroom_member:：  班级里有哪些学生            {"1班": ["sb", "cz", "haha"], "2班": ["cz"], "3班": ["pl"]}
    new_class：          课程列表                    语文|数学|英语|体育|地理|linux|python|
    new_classroom：      班级列表                    1班|2班|3班|
    new_user：           用户列表                    admin|123|admin     sb|123|member       zz|123|teacher      
    tea_classroom：      讲师代了哪些班级            {"zz": ["1班", "2班"], "ad": ["2班", "3班", "1班", "1班"]}
    user_class：         学员选了哪些课               {"cz": ["语文", "数学", "英语", "体育", "地理", "linux"]}
    '''
)



class student:
    gg = {"查看课程": 'list_class', '选择课程': 'choose_class', "查看所选课程": 'list_stu_class', "退出": 'exit'}

    def __init__(self, name):
        self.name = name

    # 查看课程
    def list_class(self):
        # 打开课程列表的存储文件
        with open("new_class", 'r', encoding="utf8") as f_read_class:
            tmp = {}
            #将课程列表通过枚举放入字典
            for index, i in enumerate(f_read_class.read().split("|"), 1):
                print(index, i)
                tmp[str(index)] = i
            # print(tmp)
            return tmp

    def choose_class(self):
        #打印课程列表字典，列出课程列表+序号
        tmp = self.list_class()
        stu_choose_class = input("请选择你要选的课程的序号:")
        #如果用户输入课程列表在字典中
        if stu_choose_class in tmp:
            #打开学员选课文件
            with open("user_class", 'r', encoding="utf8") as f:
                #将文件中内容通过json序列化出来，赋值给user_class
                user_class = json.load(f)
                # 如果self.name在user_class的key中   {"cz": ["语文"]}
                if user_class.get(self.name):
                    #将用户选择的课程序号对应的课程添加到user_class的对应value中
                    user_class.get(self.name).append(tmp[stu_choose_class])
                else:
                    # 如果self.name没有在user_class的key中   {"cz": ["语文"]}
                    # 那么使用setdefault将self.name:[用户选择的课程序号对应的课程]初始化进去
                    user_class.setdefault(self.name, [tmp[stu_choose_class]])
            #写入文件
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


class teacher:
    gg = {"查看所有课程": 'list_class', '查看所教班级': 'list_tea_classroom', "查看班级中的学生": 'list_classroom_stu', "退出": 'exit'}

    def __init__(self, name):
        self.name = name

    def list_class(self):
        with open("new_class", 'r', encoding="utf8") as f_read_class:
            tmp = {}
            for index, i in enumerate(f_read_class.read().split("|"), 1):
                print(index, i)
                tmp[str(index)] = i
            # print(tmp)
            return tmp

    def list_tea_classroom(self):
        with open("tea_classroom", 'r', encoding="utf8") as f:
            tea_class = json.load(f)
            stu_list = tea_class.get(self.name)
            stu_list = list(set(stu_list))
            print(stu_list)

    def a_list_classroom(self):
        print('查询所有班级')
        with open("new_classroom", 'r', encoding="utf8") as f_read_class:
            tmp = {}
            for index, i in enumerate(f_read_class.read().split("|"), 1):
                print(index, i)
                tmp[str(index)] = i
            return tmp

    def list_classroom_stu(self):
        tmp=teacher.a_list_classroom(self)
        chooise_classroom=input('请输入查询班级：')
        if chooise_classroom in tmp:
            with open("classroom_member", 'r', encoding="utf8") as f:
                list_member = json.load(f)
                classroom_list = list_member.get(tmp[chooise_classroom])
                classroom_list = list(set(classroom_list))
                print(classroom_list)

    def tea_exit(self):
        exit()


class admin:
    gg = {"创建课程": 'a_create_class', '创建学生学生账号': "a_create_account", "查看所有课程": "a_list_class", "查看所有学生": "a_list_stu",
                "查看所有学生的选课情况": "a_list_stu_class", '创建讲师': "create_teacher", "为讲师指定班级": "tracher_classroom", "创建班级": "create_classroom",
                "为学生指定班级": "student_classroom", '退出程序': "admin_exit"}
    def __init__(self, name):
        self.name = name

    def a_create_class(self):
        create_class = input('请输入新增的课程：')
        with open('new_class', encoding='utf-8', mode='a')as f_create_class:
            f_create_class.write(create_class + '|')
            print('{}课程创建成功！'.format(create_class))

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
                f_register.write(register_user_name + '|' + register_password + '|' + 'member' '\n')
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
                login_line = i.strip().split('|')
                if login_line[2] == 'member':
                    print(i.strip().split('|')[0])

    def a_list_stu_class(self):
        list_stu_name = input('请输入查询学生姓名：')
        with open("user_class", 'r', encoding="utf8") as f:
            user_class = json.load(f)
            stu_list = user_class.get(list_stu_name)
            stu_list = list(set(stu_list))
            print(stu_list)

    def create_teacher(self):
        create_teacher=input('请输入需要创建的讲师：')
        teacher_password = input('请输入您需要注册的讲师密码：')
        with open('new_user', encoding='utf-8', mode='r+')as f_teacher:
            for line in f_teacher:
                user_info = line.split('|')
                if create_teacher in user_info:
                    print('用户已存在,请重新输入')
                    # continue
            else:
                f_teacher.write(create_teacher + '|' + teacher_password + '|' + 'teacher' + '\n')
                print('{}讲师注册成功'.format(create_teacher))

    def a_list_tea(self):
        print('查询所有讲师')
        with open('new_user', encoding='utf-8')as f_list_stu:
            for i in f_list_stu:
                login_line = i.strip().split('|')
                if login_line[2] == 'teacher':
                    print(i.strip().split('|')[0])

    def create_classroom(self):
        create_classroomn = input('请输入需要创建的班级：')
        with open('new_classroom', encoding='utf-8', mode='r+')as f_classroom:
            for line in f_classroom:
                user_info = line.split()
                if create_classroomn in user_info:
                    print('班级已存在,请重新输入')
                    # continue
            else:
                f_classroom.write(create_classroomn + '|')
                print('{}班级创建成功'.format(create_classroomn))

    def a_list_classroom(self):
        print('查询所有班级')
        with open("new_classroom", 'r', encoding="utf8") as f_read_class:
            tmp = {}
            for index, i in enumerate(f_read_class.read().split("|"), 1):
                print(index, i)
                tmp[str(index)] = i
            return tmp

    def tracher_classroom(self): # 为讲师指定班级
        tea = admin.a_list_tea(self)
        tea_name = input("请输入讲师:")
        tmp = admin.a_list_classroom(self)
        tea_choose_classroom = input("请选择你要选的班级的序号:")
        if tea_choose_classroom in tmp:
            with open("tea_classroom", 'r', encoding="utf8") as f:
                tea_classroom = json.load(f)
                # print(tea_classroom, type(tea_classroom))
                if tea_classroom.get(tea_name):
                    tea_classroom.get(tea_name).append(tmp[tea_choose_classroom])
                    print('为{}老师指定为{}班代课老师成功！'.format (tea_name,tmp[tea_choose_classroom]))
                else:
                    tea_classroom.setdefault(tea_name, [tmp[tea_choose_classroom]])
                    print('为{}老师指定为{}班代课老师成功！'.format(tea_name, tmp[tea_choose_classroom]))

            with open("tea_classroom", 'w', encoding="utf8") as f:
                json.dump(tea_classroom, f, ensure_ascii=False)


    def student_classroom(self): #为学生指定班级
        stu = admin.a_list_stu(self)
        stu_name = input("请输入学生:")
        tmp = admin.a_list_classroom(self)
        stu_choose_classroom = input("请选择为学生指定班级的序号:")
        print(tmp)
        if stu_choose_classroom in tmp:
            with open("classroom_member", 'r', encoding="utf8") as f:
                classroom_member = json.load(f)
                if classroom_member.get(tmp[stu_choose_classroom]):
                    print(classroom_member.get(tmp[stu_choose_classroom]))
                    classroom_member.get(tmp[stu_choose_classroom]).append(stu_name)
                else: #不存在如何初始化
                    classroom_member.setdefault(tmp[stu_choose_classroom], [stu_name])

            with open("classroom_member", 'w', encoding="utf8") as f:
                json.dump(classroom_member, f, ensure_ascii=False)
    
    def admin_exit(self):
        exit()


def login():
    print('欢迎来到选课系统！')
    count = 1
    while count < 4:
        print('请先登录')
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        with open('new_user', encoding='utf8')as f_registry:
            for i in f_registry:
                login_line = i.strip().split('|')
                if username == login_line[0] and password == login_line[1]:  # z 123 member zz 234 admin
                    if login_line[2] == 'admin':
                        print('管理员%s登录成功！' % (username))
                        admin_user = admin(username)
                        # admin_user.show()
                        while 1:
                            tmp = {}
                            for index, i in enumerate(admin_user.gg, 1):
                                print(index, i)
                                tmp[str(index)] = admin_user.gg[i]
                            C = input("请输入你的选择：")  # 根据不同的选择, 执行不同的函数
                            func = getattr(admin_user, tmp[C])
                            func()
                        # return
                    elif login_line[2] == 'member':
                        print('学员%s登录成功！' % (username))
                        student_user = student(username)
                        while 1:
                            tmp = {}
                            for index, i in enumerate(student_user.gg, 1):
                                print(index, i)
                                tmp[str(index)] = student_user.gg[i]
                            C = input("请输入你的选择：")  # 根据不同的选择, 执行不同的函数
                            func = getattr(student_user, tmp[C])
                            func()
                        # student_user.show()
                        # return
                    elif login_line[2] == 'teacher':
                        print('讲师%s登录成功！' % (username))
                        teacher_user = teacher(username)
                        while 1:
                            tmp = {}
                            for index, i in enumerate(teacher_user.gg, 1):
                                print(index, i)
                                tmp[str(index)] = teacher_user.gg[i]
                            C = input("请输入你的选择：")  # 根据不同的选择, 执行不同的函数
                            func = getattr(teacher_user, tmp[C])
                            func()
                        # return

            else:
                print('用户名或密码错误，请重新输入，您还有{}次机会'.format(3 - count))
                count += 1

login()