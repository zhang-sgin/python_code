# l1 = [('alex', 3), ('太白', 1), ('wS', 2), ('wS', 4)]
# def func(x):
#     return x[1]
# new_l = sorted(l1,key=func,reverse=True)
# print(new_l)


# l1=[1,2,3,4,5]
# def func(x):
#     return x % 2 == 0
# print(list(filter(func,l1)))


# l1=[1,2,3,4,5]
# def func(x):
#     return x ** 2
# print(list(map(func,l1)))

# func3  = lambda x,y,z:(x+y-z)*2
# print(func3(10,2,3))


# dic={'k1': 10, 'k2': 100, 'k3': 30}
# # print(max(dic))
# # print(dic[max(dic,key=lambda x:dic[x])])
#
#
# def func(x):
#     return dic[x]
#
# # ret = max(dic,key=func)
# ret = max(dic,key=lambda x:dic[x])
# print(ret)

#
# import sys
# sys.setrecursionlimit(100000)
# def func(x):
#     print(x)
#     x+=1
#     func(x)
# func(1)


# 1。类 静态属性 方法 对象
#
# 对象是重新生成了空间

#
# class game_role:
#     def __init__(self,name,sex,ad,hp):
#         self.name = name
#         self.sex = sex
#         self.ad = ad
#         self.hp = hp
#
# gailun=game_role('zz','man',1,10)
# print(gailun.name)


class game_role:
    a1 = 'lol'
    # def __init__(self,name,sex,ad,hp):
    def __init__(self,name,sex,ad,hp):
        self.name = name
        self.sex = sex
        self.ad = ad
        self.hp = hp
    
    def fight(self,role1):
        role1.hp = role1.hp - self.ad
        print('%s攻击了%s,%s还剩余%s血量'%(self.name,role1.name,role1.name,role1.hp))
    def equit_weapon(self,wea):
        self.wea = wea
    
class weapon:
    def __init__(self,name,ad):
        self.name = name
        self.ad = ad
    def wea_attack(self,role1,role2):
        role2.hp = role2.hp - self.ad
        print('%s用%s攻击了%s,%s还剩余%s血量'%(role1.name,self.name,role2.name,role2.name,role2.hp))
    
p1=game_role('zz','man',50,200)
p2=game_role('sb','man',60,500)
sword=weapon('宽剑',70)

p1.equit_weapon(sword)
p1.wea.wea_attack(p1,p2)