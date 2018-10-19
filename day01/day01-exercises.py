'''
1、简述变量命名规范
'''
# 变量命名规范
# 1.变量必须要要有数字，字母，下划线任意组成
# 2.变量需要具有可描述性
# 3.变量命名不能过长，不能以数字开头，不能包含中文，不能包含python关键字
# 4.推荐1,使用驼峰体:ZhangZheng = me
#  推荐2:使用下划线:my_name_ha = zz

'''
2.name = input(">>>") name变量是什么数据类型？
'''
# name = input(">>>")
# str转换为int
# name = int(name)
# print(name,type(name))
# input输入的数据类型在没有转换的情况下，都是是字符串str类型

'''
3、if条件语句的基本结构?
'''
# if条件语句基本结构有5种
# A.if
#if 2 > 3:
#    print(nb)

#B.if...else 二必选一

# age = input("how old are you?")
# if age == '13':
#     print("T")
# else:
#     print("F")
#
# name = input("what's your name?")
# if name == 'zhangzheng':
#     print('nb')
# else:
#     print('sb')

#C.if...elif...elif
# age = input('how old are you?')
# if age == '18':
#     print('18真好')
# elif age == '20':
#     print('20不错')
# elif age == '25':
#     print('25也行')

#D.if...elif..elif...else
# age = input('how old are you?')
# if  age == '18':
#     print('18真好')
# elif age == '25':
#     print('25也还行')
# elif age == '30':
#     print('sb')
# else:
#     if age <= '17':
#         print('谢谢夸奖')
#     elif age >= '31':
#         print('滚你大爷')

#E.if嵌套
# name = input("who's your name?")
# age = input('how old are you?')
# if name == 'zz':
#     if age == '20':
#         print('说得对')
#     else:
#         age >= '20'
#         print('请重新输入')
#         print('您还有3次机会')
# else:
#     print('用户名错误')

'''
4、⽤print打印出下⾯内容：
⽂能提笔安天下,
武能上马定乾坤.
⼼存谋略何⼈胜,
古今英雄唯是君.
'''

# mes='''
# ⽂能提笔安天下,
# 武能上马定乾坤.
# ⼼存谋略何⼈胜,
# 古今英雄唯是君.
# '''
# print(mes)

'''
5、利⽤if语句写出猜⼤⼩的游戏：
设定⼀个理想数字比如： 66， 让⽤户输入数字， 如果比66⼤， 则显⽰猜测的结果
⼤了； 如果比66⼩， 则显⽰猜测的结果⼩了;只有等于66， 显⽰猜测结果正确。
'''
# num = input('请输入预测的数字:')
# num = int(num)
# if num == 66:
#     print('猜测结果正确')
# elif num <= 65:
#     print('猜测数值过小，请重新输入！')
# elif num >= 67:
#     print('猜测数值过大，请重新输入！')

'''
6、提⽰⽤户输入他的年龄, 程序进⾏判断.
如果⼩于10, 提⽰⼩屁孩,
如果⼤于10, ⼩于 20, 提⽰青春期叛逆的⼩屁孩.
如果⼤于20, ⼩于30. 提⽰开始定性, 开始混社会的⼩屁孩⼉,
如果⼤于30, ⼩于40. 提⽰看老⼤不⼩了, 赶紧结婚⼩屁孩⼉.
如果⼤于40, ⼩ 于50. 提⽰家⾥有个不听话的⼩屁孩⼉.
如果⼤于50, ⼩于60. 提⽰⾃⼰马上变成不听 话的老屁孩⼉.
如果⼤于60, ⼩于70. 提⽰活着还不错的老屁孩⼉.
如果⼤于70, ⼩于 90. 提⽰⼈⽣就快结束了的⼀个老屁孩⼉.
如果⼤于90以上. 提⽰. 再见了这个世界.
'''

# age = int(input('how old are you?'))
# if age <= 10:
#     print('小屁孩')
# elif age <= 20:
#     print('青春期叛逆的⼩屁孩')
# elif age <= 30:
#     print('开始定性, 开始混社会的⼩屁孩⼉')
# elif age <= 40:
#     print('老⼤不⼩了, 赶紧结婚⼩屁孩⼉')
# elif age <= 50:
#     print('家⾥有个不听话的⼩屁孩⼉')
# elif age <= 60:
#     print('⾃⼰马上变成不听 话的老屁孩⼉')
# elif age <= 70:
#     print('活着还不错的老屁孩⼉')
# elif age > 90:
#     print('再见了这个世界')

'''
7、单⾏注释以及多⾏注释？
'''
# 注释为了帮助解释说明
# 单行注释：#
# 多行注释:'''被注释内容''' """被注释内容"""

'''
8、简述你所知道的Python3x和Python2x的区别？
'''
# python2.x:
# 1.默认ACISS编码
# 2.print'haha'
# 3.input内容数据类型为int
# python3.x:
# 1.默认utf-8
# 2.print('hh')
# 3.input内容数据类型为str

'''
9、提⽰⽤户输入⿇花藤. 判断⽤户输入的对不对. 如果对, 提⽰真聪明, 如果不对, 提
⽰你 是傻逼么
'''
# name = input('请输入您的用户名:')
# if name == '麻花藤':
#     print('真聪明')
# else:
#     print('你是傻逼么')

'''
10、使⽤while循环输入 1 2 3 4 5 6 8 9 10
'''

num = 1
while num < 11:
    if num == 7:
        num = num + 1
        continue
    print(num)
    num = num + 1

'''
11、求1-100的所有数的和
'''
# a = 0
# b = 1
# while b < 101:
#     a = a + b
#     b = b + 1
# print(a)

'''
12、输出 1-100 内的所有奇数
'''
# num = 1
# while num < 100:
#     print(num)
#     num = num + 2

# cont=1
# while cont < 99:
#     if cont % 2 == 1:
#         cont = cont + 2
#         print(cont)


'''
13、输出 1-100 内的所有偶数
'''
# num = 0
# while num < 100:
#     print(num)
#     num = num + 2

# cont=0
# while cont < 100:
#     if cont % 2 ==0:
#         cont = cont + 2
#         print(cont)

'''
14、求1-2+3-4+5 ... 99的所有数的和
'''
# num = 0
# count = 0
# while num < 99:
#     num = num +1
#     if num % 2 ==0:
#         count = count - num
#     else:
#         count = count + num
# print(count)

# num = 0
# for i in range(100):
#     if i % 2 == 0:
#         num = num - i
#     else:
#         num = num + i
# print(num)