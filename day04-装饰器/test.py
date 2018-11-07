# import time
# def func1():
#     time.sleep(0.6)
#     print('来了，老弟')
# #
# # def func2():
# #     time.sleep(0.5)
# #     print('回手 掏 ，走位走位....')
#
# def timmer(f):
#     def inner():
#         start_time = time.time()
#         f()
#         end_time = time.time()
#         print('此函数的执行时间是%s' % (end_time-start_time))
#     return inner
# func1 = timmer(func1)
# # func1()
#
#
#
#
# def func3():
#     print(555)
#
# def func4(x):
#     def inner():
#         x()
#     return inner
# func4(func3)()

# l1=[1,2,3,'zz']
# iter1=l1.__iter__()
# while 1:
#     try:
#         print(iter1.__next__())
#     except StopIteration:
#         break
#


# def clo():
#     for i in range(1,201):
#         print('序号%s' % (i))
# # clo()
#
# def clo2():
#     for i in range(1,201):
#         yield '序号%s' % (i)
# z=clo2()
#
# for i in range(5):
#     print(z.__next__())
# for i in range(195):
#     print(z.__next__())

# l1=[]
# for i in range(1,101):
#     l1.append(i)
# print(l1)



# l1=[i for i in range(1,101)]
# print(l1)

# l1=['python%d期'% i for i in range(1,101)]
# print(l1)

#
# l1=[i**2 for i in range(1,11)]
# l2=[i**2 for i in range(1,31) if i %3 ==0]
# # print(l1)
# # print(l2)
#
# l1=['alex','taibai','wusir','ab','sb']
# l3=[i.upper() for i in l1 if len(i)>3]
# print(l3)

with open('registry2.txt', encoding='utf8')as f_registry:
    for i in f_registry:
        login_line=i.strip().split()
        print(login_line)





# login_line=[]
# with open('registry2.txt', encoding='utf8')as f_registry:
#     for i in f_registry:
#         login_line.append(i.strip().split())
#     for i2 in login_line:
#             print(i2)




#
# login_status={'username':None,'status':False}
# def login(x):
#     def inner(*args,**kwargs):
#         if login_status['status']:
#             ret = x(*args,**kwargs)
#             return ret
#         else:
#             count = 1
#             while count <4:
#                 print('请先登录')
#                 username=input('请输入用户名：').strip()
#                 password=input('请输入密码：').strip()
#                 with open('registry.txt',encoding='utf8')as f_registry:
#                     for i in f_registry:
#                         login_line=i.strip().split(' ')
#                         print(login_line)
#                         for i2 in login_line:
#                             print(i2)
#                             if username == login_line[0] and password ==login_line[1]:
#                                 login_status['username'] = username
#                                 login_status['status'] = password
#                                 ret=x(*args,**kwargs)
#                                 return ret
#                             else:
#                                 print('用户名或密码错误，请重新输入，您还有{}次机会'.format(3 - count))
#                                 count += 1
#     return inner
#
# @login
# def nice():
#     print('漂亮，nice打印成功')
#
#
# @login
# def perfect():
#     print('漂亮,perfect打印成功')
#
# dic = {
#     1: nice,
#     2: perfect,
# }
#
# while 1:
#     print('''
#     1.nice
#     2.perfect
#     ''')
#     num = input('请输入数字：').strip()
#     dic[int(num)]()