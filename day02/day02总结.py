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
# <<<<<<< HEAD

'''
三：编码初识别
编码：
"北京烤鸭降价了"
对照表：密码本
    0000001  北
    0000100  京
    0010110  烤
    0010101  鸭

0010100 0101100 10101

ASCII:最早版本的'密码本'.
    8位 == 1 个字节。
    0000 0001 256可能，代表256个不同的字符。
    ABC：
    01000001 01000010 01000011
    一个字符：1个字节表示。
    'hello': 5个字节

万国码：Unicode，将世界上所有国家的文字都包含进来。
    起初：16位 两个字节表示一个字符。
        a: 01000001 01000001
        中：01000101 01000001
    升级：32位 四个字节表示一个字符。
        a: 01000001 01000001 01000001 01000001
        中：01000101 01000001 01000001 01000001
    浪费资源，空间。

utf-8:最少用8位，一个字节表示一个字符。
           a:01000001 一个字节
    欧洲文字: 01000001 01000001 两个字节
    亚洲 中 ：01000001 01000001 01000001 三个字节。

gbk: 国标，只包含ASCII，中文。
    a: 01000001 一个字节
    中:01000001 01000001 两个字节。

s1 = '老男boy'
# gbk 编码：7个字节。
# utf-8 编码：9个字节。

单位转换：
    8bit == 1 bytes
    1024bytes == 1 kb
    1024kb == 1MB
    1024MB = 1Gb
    1024GB = 1TB
    1024TB = 1PB
'''

'''
四：数据类型：int bool str list tuple dict
'''
'''1.int'''
# i = 10
# i1 = 6
# print(i.bit_length())
# print(i1.bit_length())
# bit_length() 计算十进制转换为二进制的有效位数

'''2.bool True False'''
# str ---> boot str的值非空，就是True
# s1 = 'zz'
# s2 = ' '
# s3 = ''
# print(bool(s1))
# print(bool(s2))
# print(bool(s3))
# s = input('>>>')
# if not s:
#     print('此处数据不能为空')
# else:
#     print('ok')

# bool ---> str
# print(str(True),type(str(True)))

'''3. str'''
# 3.1索引以及切片
# s = 'python24期'
# 下标，索引
# s1 = s [-1]
# s2 = s [8]
# print(s2,type(s2))

# 3.2 切片 顾头不顾腚
# s [起始索引：'结尾索引+1':步长]
# print(s[0:2])   print(s[:2])
# print(s[:6])
# print(s[:]) print(s[0:0])
# print(s[:6:2]) print(s[0:6:2])  意思是从索引0-6之间，步长为2进行切片
# print(s[-1:-4:-1]) 意思是从索引-1到-4，步长为1进行切片

# 常用方法： 对字符串操作形成的都是新的字符串
# zz = 'zhangZheng'

# capitalize()   首字母大写，其他字母小写 *
# z1 = zz.capitalize()
# print(z1)

# swapcase() 大小写反转 *
# z2 = zz.swapcase()
# print(z2)

# center 居中，设置宽度 *
# z3 = zz.center(20,"*")
# print(z3)

# da = 'zz dadadad%dasd*fasfad()dada'
# title() 非字母隔开的‘单词’ 首字母大写 *
# z4 = da.title()
# print(z4)

# zz = input('请输入用户名：')
# upper() 全大写 **
# lower() 全小写 **
# z5 = zz.upper()
# z6 = zz.lower()
# print(z5)

'''
模拟验证码登录

username = input('请输入用户名：')
password = input('请输入密码：')
code = 'zhangdage'.upper()
your_code = input('请输入验证码：').upper()
if  username == 'zz' and password == '123' and your_code == code:
    print('登录成功')
'''
# startswith()判断以什么开头 **
# endswith() 判断以什么结尾 **
# z7 = zz.startswith('z')
# z8 = zz.endswith('g')
# z8 = zz.endswith('Z',-6)
# print(z8)

# zz = '         zhangzheng \t    '
# strip() 默认去除str前后两端换行符，制表符，空格。 ***
# lstrip() 只去除左边空格
# zz.rstrip() 只去除右边空格
# z9 = zz.strip()
# z9 = zz.lstrip()
# z9 = zz.rstrip()
# print(z9)
'''
登录时，去除用户输入用户名时附带的空格

username = input('请输入用户名：').strip()
password = input('请输入密码：').strip()
if username == 'zz' and password == '123':
    print('登录成功')
'''

# z = 'alex wusir barry'
# zz = 'alex,wusir,barry'
# zz1 = ',alex,wusir,barry'
'''str --->list *** 字符串转成列表'''
# split() 默认按照空格分割
# z1  = z.split()
# z2 = zz.split(',')
# print(z1)
# print(zz1.split(',',1))

# zz = 'oldboy'
# join 插入字符串
# z1 = '-'.join(zz)
# print(z1)

# list--->str   列表转换成字符串
# l1 = ['alex', 'wusir', 'barry'] # --> s = 'alex wusir barry'
# z = ' '.join(l1)
# print(z)

# s = '老男孩 老男孩 alex linux python 大数据 alex'
# z1 = s.replace('alex','太白')把所有alex替换成太白
# z2 = s.replace('alex','太白',1)把alex替换成太白，只执行一次
# print(z1)
# print(z2)

'''is系列----***'''
name = '123'
# print(name.isalnum())#字符串由字母或数字组成
# print(name.isalpha())#字符串只由字母组成
print(name.isdigit())#字符串只由数字组成 str ---> int 可以作为一个判断条件

'''格式化输出 format-----***'''
# res = '{} {} {}'.format('egon', 18, 'male')
# res2 = '{2} {2} {2}'.format('egon', 18, 'male')中括号内的数字是format中的索引
# res3 = '{name} {age} {sex}'.format(sex='male',name='egon',age='15') 以特殊标识格式化输出
# print(res3)

# s = 'oldboy'
# find 通过元素找索引，找不到返回-1 ***
# index 通过元素找索引，找不到报错 ***
# print(s.find('d'))
# print(s.find('o'))
# print(s.find('A'))
# print(s.index('d'))
# print(s.index('A'))

'''公共方法'''
# s = 'dadazczcxjfkasdfjklsdfjl'
# print(len(s)) 测试字符串长度
# print(s.count('d')) 计算某些元素出现的次数
# =======
# >>>>>>> b1cae9f369e16ee8d1bcd147c1a09359900cec68
