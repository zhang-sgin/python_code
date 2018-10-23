'''
一：格式化输出
1).占位符
数据类型:
s：字符串
d：整数
f：浮点型
r：内置函数会讲到

格式化输出第一种方式：
'''
# name = input('请输入姓名：')
# age = int(input('请输入年龄：'))
# job = input('请输入工作：')
# hobby = input('请输入爱好：')
# msg = """
# ------------ info of %s -----------
# Name  : %s
# Age   : %d
# job   : %s
# Hobby: %s
# ------------- end -----------------
# """ % (name, name, age, job, hobby)
# print(msg)
'''
格式化输出第二种方式：
'''
# test =  {"name": 'zz', "age" : 15, "job" : 'wu' ,"hobby" : 'ai'}
# msg = """
# ------------ info of %s -----------
# Name  : %(name)s
# Age   : %(age)d
# job   : %(job)s
# Hobby: %(hobby)s
# ------------- end -----------------
# """ % test
# print(msg)

'''
如果格式化输出的时候，只想单纯的想要表示 %  使用两个%%
'''
# msg = '我叫%s，今年%d，学习进度5%%' % ('zz',15)
# # print(msg)


'''
二：运算符
'''

# 1.算数运算： + - * / % **.
a = 10
b = 3
# print(a / b)
# print(a % b)
# print(2 ** 2)
# print(a // b)

# 2.比较运算： == != > < >= <=
# print(a < b)

# 3.赋值运算： += -= * / % **
# b += a
# b -= a
# b *= a
# b /= a
# b **=a
# b //= a
# print( b)

# 4.逻辑运算 not and or
# 逻辑运算优先级: () not and or 同一优先级从左往右依次计算
# 4.1 逻辑运算两边都是比较
# print(3 > 2 and 3 < 4 or 5 > 6 and 2 <5)
# print(1 > 1 and 3 < 5 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# print( True or False)

# 4.2 逻辑运算两边都是数值
# x or y ,if x is True, return x,else return y.
# print(1 or 3)
# print(100 or 3)
# print(-10 or 3)
# print(0 or 3) 0为False,所以输出3

# x and y ,if x is True, return y,else return x.
# print(1 and 3 or 4)
# print(0 and 3 or 5)

# int bool 之间的转换
# int ---> boot:非零即True
# print( bool(100))

# bool ---> int: True 1,False 0
# print(int(True))
# print(int(False))

# 4.3逻辑运算两边是数值或者比较
# print( 1 and 4 < 6 or 5)

'''
成员运算，判断某些元素在不在一个序列中，str tuple list dict  set
in
not in
'''
# s1 = 'ab'
# s11 = 'ak'
# s2 = 'dasdasdaabsdaakdada'
# print(s1 in s2)
# print(s11 in s2)
# conment = input('>>>')
# s1 = 'tmd'
# print( 2 ** 32)
