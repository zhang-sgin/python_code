'''
1,完成下列功能:
  1.1创建一个人类Person,再类中创建3个静态变量(静态字段)
    animal = '高级动物'
    soul = '有灵魂'
    language = '语言'
  1.2在类中定义三个方法,吃饭,睡觉,工作.
  1.3在此类中的__init__方法中,给对象封装5个属性:国家,姓名,性别,年龄,  身高.
  1.4实例化四个人类对象:
    第一个人类对象p1属性为:中国,alex,未知,42,175.
    第二个人类对象p2属性为:美国,武大,男,35,160.
    第三个人类对象p3属性为:你自己定义.
    第四个人类对象p4属性为:p1的国籍,p2的名字,p3的性别,p2的年龄,p3  的身高.
  1.5 通过p1对象执行吃饭方法,方法里面打印:alex在吃饭.
  1.6 通过p2对象执行吃饭方法,方法里面打印:武大在吃饭.
  1.7 通过p3对象执行吃饭方法,方法里面打印:(p3对象自己的名字)在吃饭.
  1.8 通过p1对象找到Person的静态变量 animal
  1.9 通过p2对象找到Person的静态变量 soul
  2.0 通过p3对象找到Person的静态变量 language
'''
# class Person:
#     animal = '高级动物'
#     soul = '有灵魂'
#     language = '语言能力'
#
#     def __init__(self,country,name,sex,age,hight):
#         self.country = country
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.hight = hight
#
#     def eat(self):
#         return "%s在吃饭" % self.name
#
#     def sleep(self):
#         return "%s在睡觉" % self.name
#     def work(self):
#         return "%s在工作"
# p1=Person('中国','alex','未知',41,175)
# p2=Person('美国','武大','男',35,165)
# p3=Person('中国','zz','男',18,185)
# p4=Person(p1.country,p2.name,p3.sex,p2.age,p3.hight)
#
# print(p1.eat())
# print(p2.eat())
# print(p3.eat())
#
# print(p1.animal)
# print(p2.soul)
# print(p3.language)



'''
2,通过自己创建类,实例化对象
  在终端输出如下信息
  小明，10岁，男，上山去砍柴
  小明，10岁，男，开车去东北
  小明，10岁，男，最爱大保健
  老李，90岁，男，上山去砍柴
  老李，90岁，男，开车去东北
  老李，90岁，男，最爱大保健
  老张…
'''

# class Person:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def kc(self):
#         return "%s,%s岁,%s,上山去砍柴" % (self.name, self.age, self.sex)
#
#     def qdb(self):
#         return "%s,%s岁,%s,开车去东北" % (self.name, self.age, self.sex)
#
#     def dbj(self):
#         return "%s,%s岁,%s,最爱大保健" % (self.name, self.age, self.sex)
# xm=Person('小明',10,'男')
# li=Person('老李',90,'男')
# print(xm.kc())
# print(xm.qdb())
# print(xm.dbj())
# print(li.kc())
# print(li.qdb())
# print(li.dbj())


'''
3,模拟英雄联盟写一个游戏人物的类（升级题）.
  要求:
  (1)创建一个 Game_role的类.
  (2) 构造方法中给对象封装name,ad(攻击力),hp(血量).三个属性.
  (3) 创建一个attack方法,此方法是实例化两个对象,互相攻击的功能:
      例: 实例化一个对象 盖伦,ad为10, hp为100
      实例化另个一个对象 剑豪 ad为20, hp为80
      盖伦通过attack方法攻击剑豪,此方法要完成 '谁攻击谁,谁掉了多少血,  还剩多少血'的提示功能.
'''
class game_role:
    def __init__(self, name, ad, hp):
        self.name = name
        self.ad = ad
        self.hp = hp

    def fight(self, role1):
        role1.hp = role1.hp - self.ad
        print('%s攻击了%s,%s还剩余%s血量' % (self.name, role1.name, role1.name, role1.hp))

p1 = game_role('盖伦', 10, 100)
p2 = game_role('剑豪', 20, 80)
# game_role.fight(p1,p2)
# print(p1.name)
'''
1，暴力摩托程序（完成下列需求）：
1.1创建三个游戏人物，分别是：
•	苍井井，女，18，攻击力ad为20，血量200
•	东尼木木，男，20，攻击力ad为30，血量150
•	波多多，女，19，攻击力ad为50，血量80
1.2创建三个游戏武器，分别是：
•	平底锅，ad为20
•	斧子，ad为50
•	双节棍，ad为65

1.3 创建三个游戏摩托车，分别是：

•	小踏板，速度60迈
•	雅马哈，速度80迈
•	宝马，速度120迈。

完成下列需求（利用武器打人掉的血量为武器的ad + 人的ad）：
（1）苍井井骑着小踏板开着60迈的车行驶在赛道上。
（2）东尼木木骑着宝马开着120迈的车行驶在赛道上。
（3）波多多骑着雅马哈开着80迈的车行驶在赛道上。
（4）苍井井赤手空拳打了波多多20滴血，波多多还剩xx血。
（5）东尼木木赤手空拳打了波多多30滴血，波多多还剩xx血。
（6）波多多利用平底锅打了苍井井一平底锅，苍井井还剩xx血。
（7）波多多利用斧子打了东尼木木一斧子，东尼木木还剩xx血。
（8）苍井井骑着宝马打了骑着小踏板的东尼木木一双节棍，东尼木木哭了，还剩xx血。（选做）
（9）波多多骑着小踏板打了骑着雅马哈的东尼木木一斧子，东尼木木哭了，还剩xx血。（选做）
'''
# class Person:
#     def __init__(self, name, sex, age,ad, hp):
#         self.name = name
#         self.ad = ad
#         self.sex = sex
#         self.age = age
#         self.hp = hp
#     def k_attack(self,role1):
#         role1.hp -= role1.ad
#         return "%s赤手空拳攻击了%s%s滴血，%s还剩%s血" % (self.name,role1.name,self.ad,role1.name,role1.hp)
#
#     def game_equipment(self,equipment):
#         self.equipment=equipment
#
#     def bike(self,cars):
#         self.cars = cars
#
#
# class weapon:
#     def __init__(self,name,ad):
#         self.name = name
#         self.ad = ad
#
#     def q_attack(self,role1,role2):
#         role2.hp = role2.hp - self.ad - role1.ad
#         return "%s利用%s打了%s一%s，%s还剩%s血" % (role1.name,self.name,role2.name,self.name,role2.name,role2.hp)
#
#     def x_attack(self, p1, p2, m1, m2):
#         p2.hp = p2.hp - self.ad - p1.ad
#         return  "%s骑着%s打了骑着%s的%s一%s,%s哭了,%s还剩%s血" \
#                 % (p1.name, m1.name, m2.name, p2.name, self.name, p2.name, p2.name, p2.hp)
#
#
# class cars:
#     def __init__(self,name,speed):
#         self.name = name
#         self.speed = speed
#
#     def biaoche(self,role1):
#         return "%s骑着%s开着%s的车行驶在赛道上" % (role1.name,self.name,self.speed)
#
#
# p1=Person("苍井井","女",18,20,200)
# p2=Person("东尼木木","男",20,30,150)
# p3=Person("波多多","女",19,50,80)
#
# s1=weapon("平底锅",20)
# s2=weapon("斧子",50)
# s3=weapon("双节棍",65)
#
# m1=cars("小踏板",60)
# m2=cars("雅马哈",80)
# m3=cars("宝马",120)

# p1.bike(m1)
# print(p1.cars.biaoche(p1))
# p2.bike(m3)
# print(p2.cars.biaoche(p2))
# p3.bike(m2)
# print(p3.cars.biaoche(p3))

# print(p1.k_attack(p3))
# print(p2.k_attack(p3))

# p3.game_equipment(s1)
# print(p3.equipment.q_attack(p3,p1))
# p3.game_equipment(s2)
# print(p3.equipment.q_attack(p3,p2))

# p1.bike(m3)
# p2.bike(m1)
# p1.game_equipment(s3)
# print(p1.equipment.x_attack(p1,p2,m3,m1))
#
# p3.bike(m1)
# p2.bike(m2)
# p3.game_equipment(s2)
# print(p3.equipment.x_attack(p3,p2,m1,m2))


'''
2，定义一个类，计算圆的周长和面积。

'''
# from math import pi
# class circle:
#     def __init__(self,r1):
#         self.r1 = r1
#
#     def perimeter(self):
#         return 2 * pi * self.r1
#
#     def area(self):
#         return pi * self.r1 * self.r1
# r1=circle(4)
# print(r1.perimeter())
# print(r1.area())

'''
3，定义一个圆环类，计算圆环的周长和面积（升级题）。
'''
# class round:
#     def __init__(self,r1,r2):
#         self.r1 = r1
#         self.r2 = r2
#
#     def perimeter(self,r1,r2):
#         p1 = r1 * 2 * 3.14
#         p2 = r2 * 2 * 3.14
#         return p1 + p2
#
#     def area(self,r1,r2):
#         a1 = r1 * r1 * 3.14
#         a2 = r2 * r2 * 3.14
#         return a1 - a2
# p=round(20,10)
# print(p.perimeter(20,10))
# print(p.area(20,10))

'''
一，简答题：
1，面向对象的三大特性是什么？
1.它是将某些相关的功能（函数）封装到了一起。
2.继承
3.多态
2，什么是面向对象的新式类？什么是经典类？
新式类默认继承object，经典类默认不继承object
3，面向对象为什么要有继承？继承的好处是什么？
提高代码复用性，可维护性，类与类之间产生关系是多态的前提
4，面向对象中super的作用。
调用父类
'''


'''
二，代码题(通过具体代码完成下列要求)：
1，
a,定义一个父类Animal，在构造方法中封装三个属性，姓名，性别，年龄，再给其添加一个eat的方法，方法中显示%s正在吃饭（%s是哪个对象调用此方法，显示哪个对象名字）。
b,定义两个基类Person,Dog，全部继承这个父类Animal.
c,Person类中，有构造方法，封装一个皮肤的属性，有eat方法，方法中显示人类正在吃饭。
d,Dog类中，有构造方法，封装一个毛色的属性，有eat方法，方法中显示狗狗正在吃饭。
上面这几个类创建完成之后，完成下列要求：
①： 实例化一个人类的对象，让其只封装皮肤属性。
②： 实例化一个人类的对象，让其封装姓名，性别，年龄，皮肤四个属性。
③： 实例化一个狗类的对象，让其只封装毛色属性。
④： 实例化一个狗类的对象，让其封装姓名，性别，年龄，毛色四个属性。
⑤： 实例化一个人类的对象，让其只执行父类的eat方法（可以对人类代码进行修改）。
⑥： 实例化一个狗类的对象，让其既执行父类的eat方法，又执行子类的eat方法。
'''
# class Animal:
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self):
#         return  "%s正在吃饭" % self.name
#
# class Person(Animal):
#     def __init__(self,skin,name,sex,age):
#         self.skin = skin
#         super(Person,self).__init__(name,sex,age)
#
#     # def eat(self):
#     #     super().eat()
#     #     return "人类正在吃饭"
#         # print('person')
#
# class Dog(Animal):
#     def __init__(self,color,name,sex,age):
#         self.color = color
#         super(Dog,self).__init__(name,sex,age)
#
#     def eat(self):
#         super().eat()
#         print(super().eat())
#         return "狗狗正在吃饭"
#
# p1=Person('黄皮肤','zz','man',18)
# d1=Dog('黑毛','dog','gong',3)
# print("1.实例化一个人类的对象，让其只封装皮肤属性。")
# print(p1.skin)
# print("2.实例化一个人类的对象，让其封装姓名，性别，年龄，皮肤四个属性。")
# print(p1.__dict__)
# print("3.实例化一个狗类的对象，让其只封装毛色属性。")
# print(d1.color)
# print("4.实例化一个狗类的对象，让其封装姓名，性别，年龄，毛色四个属性。")
# print(d1.__dict__)
# print("5.实例化一个人类的对象，让其只执行父类的eat方法（可以对人类代码进行修改）。")
# print(p1.eat())
# print("6.实例化一个狗类的对象，让其既执行父类的eat方法，又执行子类的eat方法。")
# print(d1.eat())



# class A:
#     def func(self):
#         print('in A')
#
# class B:
#     def func(self):
#         print('in B')
#
# class C(A,B):
#     def func(self):
#         print('in C')
        # super(C, self).func()
        # super(A, self).func()
# 可以改动上上面代码，完成下列需求：
# 对C类实例化一个对象产生一个c1，然后c1.func()
# print("1.让其执行C类中的func")
# class A:
#     def func(self):
#         print('in A')
#
# class B:
#     def func(self):
#         print('in B')
#
# class C(A,B):
#     def func(self):
#         print('in C')
# c1=C()
# c1.func()
# print("2，让其执行A类中的func")
# class A:
#     def func(self):
#         print('in A')
#
# class B:
#     def func(self):
#         print('in B')
#
# class C(A):
#     def __init__(self):
#         pass
# c1=C()
# c1.func()
# print("3.让其执行B类中的func")
# class A:
#     def func(self):
#         print('in A')
#
# class B:
#     def func(self):
#         print('in B')
#
# class C(B):
#     def __init__(self):
#         pass
# c1=C()
# c1.func()
# print("4.让其既执行C类中的func，又执行A类中的func")
# class A:
#     def func(self):
#         print('in A')
#
# class B:
#     def func(self):
#         print('in B')
#
# class C(A,B):
#     def func(self):
#         print('in C')
#         super(C, self).func()
# c1=C()
# c1.func()
# print("5.让让其既执行C类中的func，又执行B类中的func")
# class A:
#     def func(self):
#         print('in A')
#
# class B:
#     def func(self):
#         print('in B')
#
# class C(A,B):
#     def func(self):
#         print('in C')
#         super(A, self).func()
# c1=C()
# c1.func()

'''
3，下面代码执行结果是什么？为什么？
'''
class Parent:
    def func(self):
        print('in Parent func')

    def __init__(self):
        self.func()

class Son(Parent):
    def func(self):
        print('in Son func')

# son1 = Son()
# Son类继承Parent类，Parent中优先执行__init__方法，
# son1实例化对象时，Parent的__init__方法中self.func()的self为Son，所以self.func()=Son()

class A:
    name = []
    # age=[]
p1 = A()
p2 = A()
p1.name.append(1)
# p1.age.append(12)
p1.age = 12
'''
p1.name，p2.name，A.name 分别是什么？
p1.age = 12
p1.age，p2.age，A.age 分别又是什么？为什么？
'''
# print(p1.name)
# print(p2.name)
# print(A.name)


# print(p1.__dict__)
# print(p1.age)
# print(p2.age)
# print(A.age)
# p1是A的实例化对象，单独空间，p1.age是封装的静态属性，跟p2，A没有关系