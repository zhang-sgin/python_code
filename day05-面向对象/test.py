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
import json
import os
import sys
class student:
    def __init__(self,name):
        self.name = name

    def list_class(self):
        with open("new_class", 'r', encoding="utf8") as f_read_class:
            tmp = {}
            for index, i in enumerate(f_read_class.read().split("|"),1):
                print(index, i)
                tmp[str(index)] = i
            return tmp


    def choose_class(self):
        tmp = self.list_class()
        stu_choose_class = input("请选择你要选的课程的序号")
        if stu_choose_class in tmp:
            with open("user_class", 'r',  encoding="utf8") as f:
                user_class = json.load(f)
                if user_class.get(self.name):
                    user_class.get(self.name).append(tmp[stu_choose_class])
                else:
                    user_class.setdefault(self.name,[tmp[stu_choose_class]])

            with open("user_class", 'w', encoding="utf8") as f:
                json.dump(user_class,f,ensure_ascii=False)



    def list_stu_class(self):
        with open("user_class", 'r', encoding="utf8") as f:
            user_class = json.load(f)
            # print(user_class.get(self.name),type(user_class.get(self.name)))
            stu_list=user_class.get(self.name)
            stu_list = list(set(stu_list))
            print(stu_list)

    def exit(self):
        exit()

    def show(self):
        gongneng = {"查看课程": self.list_class, '选择课程': self.choose_class, "查看所选课程": self.list_stu_class,"退出":self.exit}
        while 1:
            tmp = {}
            for index, i in enumerate(gongneng, 1):
                print(index, i)
                tmp[str(index)] = gongneng[i]
            C = input("请输入你的选择")
            if C in tmp:
                tmp[C]()
                
class admin:
    def __init__(self,name):
        self.name=name


s=student("zz")
s.show()