import sys,threading
import random
'''
1、new方法和init方法执行的执行顺序
'''
class A:
    def __init__(self):
        self.x = 1
        print('in init')

    def __new__(cls, *args, **kwargs):
        print('in __new__')
        return object.__new__(cls)

# obj = A()
# print(obj.x)
#先执行new方法再执行init方法，
'''
2、__call__方法在什么时候被调用
'''

'''
3、请用写一个类，用反射为这个类添加一个静态属性
'''
# class A:
#     def __init__(self,are,age):
#         self.are=are
#         self.age=age
# setattr(A, 'sex','man')
# print(A.sex)

''''
4、请用反射为上题的类的对象添加一个属性name,值为你的名字
'''
# class A:
#     def __init__(self,are,age):
#         self.are=are
#         self.age=age
#
# z=A('china',18)
# haha=getattr(z,'age')
# print(haha)
#
# setattr(z,'name','zz')
# print(z.__dict__)
#
# delattr(z,'name')
# print(z.__dict__)

'''
5、请使用new方法实现一个单例模式

'''
# class A:
#     __zz = None
#     def __init__(self):
#         pass
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__zz is None:
#             obj = object.__new__(cls)
#             cls.__zz = obj
#         return cls.__zz
#
# ret1 = A()
# ret2 = A()
# ret3 = A()
# print(ret1, ret2, ret3)

# class A:
#     __A_clock = threading.Lock()
#     def __init__(self):
#         pass
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(A, "_instance"):
#             with A.__A_clock:
#                 if not hasattr(A, "_instance"):
#                     A._instance = object.__new__(cls)
#         return A._instance

# ret1 = A()
# ret2 = A()
# ret3 = A()
# print(ret1, ret2, ret3)

'''
6、生成一个6位随机验证码(包含数字和大小写字母)
'''
# def code():
#     codes=''
#     for i in range(6):
#         num = str(random.randint(0,9))
#         letter1= chr(random.randint(97,122))
#         letter2=chr(random.randint(65,96))
#         co1=random.choice([num,letter1,letter2])
#         codes += co1
#     return codes
# print(code())

'''
7、发红包、制定金额和个数随机分配红包金额
'''

# def redp():
#     money=int(input('请输入红包金额：'))
#     num=int(input('请输入红包个数：'))
#     packet=[]
#     # money100=money*100
#     while num:
#         num -= 1
#         if num == 0:
#             packet.append(money)
#             print('抢到红包%.2f元 红包抢完了!' % (money))
#         elif num > 0:
#             money100=round(random.uniform(0.01,money/num),2)
#             packet.append(money100)
#             print('抢到红包%.2f元 剩余%d个!' % (money100, num))
#             money=round(money-money100,2)
#     return
# redp()

