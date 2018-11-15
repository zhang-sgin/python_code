# class game_role:
#     a1 = 'lol'
#     # def __init__(self,name,sex,ad,hp):
#     def __init__(self,name,sex,ad,hp):
#         self.name = name
#         self.sex = sex
#         self.ad = ad
#         self.hp = hp
#
#     def fight(self,role1):
#         role1.hp = role1.hp - self.ad
#         print('%s攻击了%s,%s还剩余%s血量'%(self.name,role1.name,role1.name,role1.hp))
#     def equit_weapon(self,wea):
#         self.wea = wea
#
# class weapon:
#     def __init__(self,name,ad):
#         self.name = name
#         self.ad = ad
#     def wea_attack(self,role1,role2):
#         role2.hp = role2.hp - self.ad
#         print('%s用%s攻击了%s,%s还剩余%s血量'%(role1.name,self.name,role2.name,role2.name,role2.hp))
#
# p1=game_role('zz','man',50,200)
# p2=game_role('sb','man',60,500)
# sword=weapon('宽剑',70)
#
# p1.equit_weapon(sword)
# p1.wea.wea_attack(p1,p2)
# class GameRole:
#     def __init__(self,name,sex,age,ad,hp):
#         self.name=name
#         self.sex=sex
#         self.age=age
#         self.ad=ad
#         self.hp=hp
#     def attack(self,p):
#         p.hp-=self.ad
#         print("%s赤手空拳打了%s%s滴血,%s还剩%s血"%(self.name,p.name,self.ad,p.name,p.hp))
#
#     def game_equipment(self,equipment):
#         self.equipment=equipment
#
#     def bike(self,motorcycles):
#         self.motorcycles=motorcycles
#
#     def add_bike(self,p):
#         p.hp = p.hp - self.ad - self.equipment.ad
#         print("%s骑着%s打了骑着%s的%s一%s,%s哭了,%s还剩%s血" %\
#               (self.name,self.motorcycles.name,p.motorcycles.name,p.name,self.equipment.name,p.name,p.name,p2.hp))
# class Shop:
#     def __init__(self,name,ad):
#         self.name=name
#         self.ad=ad
#     def slaughter(self,p1,p2):
#         p2.hp=p2.hp-self.ad-p1.ad
#         print("%s利用%s打了%s一%s,%s还剩%s点血量"%(p1.name,self.name,p2.name,self.name,p2.name,p2.hp))
#     def bike_slaughter(self,p1,p2,m1,m2):
#         p2.hp = p2.hp - self.ad - p1.ad
#         print("%s骑着%s打了骑着%s的%s一%s,%s哭了,%s还剩%s血"%(p1.name,m1.name,m2.name,p2.name,self.name,p2.name,p2.name,p2.hp))
# class Motorcycles:
#     def __init__(self,name,speed):
#         self.name=name
#         self.speed=speed
#     def go_bike(self,p):
#         print("%s骑着%s开着%s迈的车行驶在赛道上"%(p.name,self.name,self.speed))
# p1=GameRole("苍井井","女",18,20,200)
# p2=GameRole("东尼木木","男",20,30,150)
# p3=GameRole("波多多","女",19,50,80)
# s1=Shop("平底锅",20)
# s2=Shop("斧子",50)
# s3=Shop("双节棍",65)
# m1=Motorcycles("小踏板",60)
# m2=Motorcycles("雅马哈",80)
# m3=Motorcycles("宝马",120)
#
#
# p1.bike(m3)
# p2.bike(m1)
# p1.game_equipment(s3)
# p1.add_bike(p2)

# p3.bike(m1)
# p2.bike(m2)
# p3.game_equipment(s2)
# p3.equipment.bike_slaughter(p3,p2,m1,m2)


# class Animal:
#     a1 = '太白'
#     def __init__(self, kind, age, sex):
#         self.kind = kind
#         self.age = age
#         self.sex = sex
#
#     def func1(self):
#         print(666)
#
# class Person(Animal):
#     pass
#
# print(Person.a1)
# Person.func1(123)

#
# class Animal:
#     def __init__(self, kind, age, sex):
#         self.kind = kind
#         self.age = age
#         self.sex = sex
#
# class Person(Animal):
#     pass
#
# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     pass

# p1 = Person('黄色人种', 25, '男')
# print(p1.__dict__)



# class Animal:
#
#     def __init__(self, kind, age, sex):
#         self.kind = kind
#         self.age = age
#         self.sex = sex
#
#     def bark(self):
#         print('动物都会叫')
#
# class Dog(Animal):
#
#     def __init__(self, k1,a1,s1,bite):
#         # Animal.__init__(self, k1, a1, s1)
#         super().__init__(k1,a1,s1)  # 自动将self传给父类的self
#         self.bite = bite
#
#     def bark(self):
#         super().bark()
#         print('汪汪汪')
#
# # d1 = Dog('藏獒', 3, '公', 300)
# # print(d1.__dict__)
# d1 = Dog('藏獒', 3, '公', 300)
# print(d1.__dict__)
# d1.bark()

# class D():
#
#     def bar(self):
#         print ('D.bar')
#
#
# class C(D):
#
#     def bar(self):
#         print('C.bar')
#
#
# class B(D):
#
#     def bar(self):
#         print('B.bar')
#
#
# class A(B, C):
#
#     def bar(self):
#         print('A.bar')
#
# a = A()
# 执行bar方法时
# 首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去C类中找，如果C类中么有，则继续去D类中找，如果还是未找到，则报错
# 所以，查找顺序：A --> B --> C --> D
# 在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
# a.bar()


import hashlib
import sys
import pickle
flag0 = True
class Course:
    def __init__(self,name,price,period,teacher):
        self.name = name
        self.price = price
        self.period = period
        self.teacher = teacher
    def __repr__(self):
        s = ''
        for k in self.__dict__:
            s += '%s :%s \n' %(k,self.__dict__[k])
        return s
class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):
    li = [('查看所有课程', 'check_all_course'), ('选择课程', 'choise_course'),
          ('查看所选课程', 'check_choise_course'), ('退出程序', 'exit_program')]

    def check_all_course(self):
        f1 = open('course_info','rb')
        while True:
            try:
                course = pickle.load(f1)
                print(course)
            except EOFError:
                break

    def choise_course(self):
        with open('stu_course','a')as f1:
            self.check_all_course()
            cous_name = input('请输入选择的课程')
            if cous_name == cous_name :
                f1.write('%s:%s\n'%(self.name,cous_name))
            else:
                print('输入错误')
    def check_choise_course(self):
        with open('stu_course')as f2:
            for line in f2:
                new_line = line.strip().split(':')
                if self.name == new_line[0]:
                    print('你已选择的课程有%s'% new_line[1])

    def exit_program(self):
        print('\033[32m退出成功\033[1m')
        global flag0
        flag0 = False


class Manager(Person):
    li = [('创建课程', 'creat_course'), ('创建学生账号', 'creat_stu_id'),
           ('查看所有课程', 'check_all_course'), ('查看所有学生', 'check_all_student'),
           ('查看所选课程', 'check_choise_course'), ('退出程序', 'exit_program')]

    def creat_course(self):
        name = input('请输入课程名：').strip()
        price = input('请输入价格：').strip()
        period = input('请输入时间周期：').strip()
        teacher = input('请输入授课老师：').strip()
        course_obj = Course(name, price, period, teacher)
        with open('course_info','ab')as f:
            pickle.dump(course_obj,f)
            # f.write('name:%s,price:%s,period:%s,teacher:%s\n' %(name,price,period,teacher))
        print('\033[33m恭喜你课程创建成功！\033[0m')


    def creat_stu_id(self):
        stu_name = input('请输入学生账号：').strip()
        stu_pwd = input('请输入学生密码：').strip()
        stu_pwd_md5 = get_pwd(stu_pwd)
        with open('userinfo','a')as f1:
            f1.write('\n%s,%s,%s' %(stu_name,stu_pwd_md5,'Student'))
        print('学生创建成功')

    def check_all_course(self):
        f = open('course_info','rb')
        while True:
            try:
                course = pickle.load(f)
                print(course)
            except EOFError:
                break
        f.close()

    def check_all_student(self):
        list = []
        with open('userinfo')as f2:
            for line in f2:
                new_line = line.strip().split(',')
                if new_line[2] == 'Student':
                    list.append(new_line[0])
            print(list)

    def check_choise_course(self):
        with open('stu_course')as f2:
            for line in f2:
                new_line = line.strip().split(',')
                print(new_line)

    def exit_program(self):
        global flag0
        print('退出成功')
        flag0 = False
        return flag0

def get_pwd(pwd):
    pwd_md5 = hashlib.md5()
    pwd_md5.update(pwd.encode('utf-8'))
    return pwd_md5.hexdigest()

def login():
    flag = True
    while flag:
        username = input('user:')
        password = input('pwd:')
        password = get_pwd(password)
        f = open('userinfo')
        for line in f:
            user,pwd,status = line.strip().split(',')
            if username == user and password == pwd:
                print('\033[1;32m登录成功\033[0m')
                f.close()
                return {'username':user,'status':status}
        else:
            print('\033[1;32m登录失败，请重新登录\033[0m')

def main():
    print('\033[1;34m欢迎进入学生选课系统\033[0m')
    ret = login()
    if ret:
        clas = getattr(sys.modules['__main__'], ret['status'])
        obj = clas(ret['username'])     # 实例化得到一个obj
        while flag0:
            for key,item in enumerate(clas.li,1):
                print(key,item[0])
            num = int(input('输入您要做的操作序号：'))
            getattr(obj,clas.li[num-1][1])()
main()