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
class GameRole:
    def __init__(self,name,sex,age,ad,hp):
        self.name=name
        self.sex=sex
        self.age=age
        self.ad=ad
        self.hp=hp
    def attack(self,p):
        p.hp-=self.ad
        print("%s赤手空拳打了%s%s滴血,%s还剩%s血"%(self.name,p.name,self.ad,p.name,p.hp))
        
    def game_equipment(self,equipment):
        self.equipment=equipment
        
    def bike(self,motorcycles):
        self.motorcycles=motorcycles
        
    def add_bike(self,p):
        p.hp = p.hp - self.ad - self.equipment.ad
        print("%s骑着%s打了骑着%s的%s一%s,%s哭了,%s还剩%s血" %\
              (self.name,self.motorcycles.name,p.motorcycles.name,p.name,self.equipment.name,p.name,p.name,p2.hp))
class Shop:
    def __init__(self,name,ad):
        self.name=name
        self.ad=ad
    def slaughter(self,p1,p2):
        p2.hp=p2.hp-self.ad-p1.ad
        print("%s利用%s打了%s一%s,%s还剩%s点血量"%(p1.name,self.name,p2.name,self.name,p2.name,p2.hp))
    def bike_slaughter(self,p1,p2,m1,m2):
        p2.hp = p2.hp - self.ad - p1.ad
        print("%s骑着%s打了骑着%s的%s一%s,%s哭了,%s还剩%s血"%(p1.name,m1.name,m2.name,p2.name,self.name,p2.name,p2.name,p2.hp))
class Motorcycles:
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
    def go_bike(self,p):
        print("%s骑着%s开着%s迈的车行驶在赛道上"%(p.name,self.name,self.speed))
p1=GameRole("苍井井","女",18,20,200)
p2=GameRole("东尼木木","男",20,30,150)
p3=GameRole("波多多","女",19,50,80)
s1=Shop("平底锅",20)
s2=Shop("斧子",50)
s3=Shop("双节棍",65)
m1=Motorcycles("小踏板",60)
m2=Motorcycles("雅马哈",80)
m3=Motorcycles("宝马",120)


p1.bike(m3)
p2.bike(m1)
p1.game_equipment(s3)
p1.add_bike(p2)

# p3.bike(m1)
# p2.bike(m2)
# p3.game_equipment(s2)
# p3.equipment.bike_slaughter(p3,p2,m1,m2)