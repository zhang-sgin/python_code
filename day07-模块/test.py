# from aaa.bbb import m2
# m2.func2()


import re
# 匹配字母（包含中文）或数字或下划线
# print(re.findall('\w', '太白jx 12*() _'))  # ['太', '白', 'j', 'x', '1', '2', '_']
# print(re.findall('\W', '太白jx 12*() _'))  # ['太', '白', 'j', 'x', '1', '2', '_']

# 匹配任意字符串/非字符串
# print(re.findall('\s', '太白jx 12*() _'))
# print(re.findall('\S', '太白jx 12*() _'))

# 匹配数字/非数字
# print(re.findall('\d', '太白jx 12*() _'))
# print(re.findall('\D', '太白jx 12*() _'))

# 从字符串开头匹配
# print(re.findall('\A太', '太白jx 12*() _'))

# 匹配字符串的结尾
# print(re.findall('666$','hello 太白金星 *-_-* \n666'))  # ['666']

# 匹配一个换行符
# 匹配一个制表符
# print(re.findall('\n', '太白jx 12*() _\n123'))
# print(re.findall('\t', '太白jx 12*() _\t334'))

s1 = '1-2*(60+(-40.35/5)-(-4*3))'

# print(re.findall('\d+', s1))
# print(re.findall('\d+\.?\d*' , s1))
# print(re.findall('-?\d+\.?\d*' , s1))



s2 ='''
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/7459977.html" target="_blank">python基础一</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/7562422.html" target="_blank">python基础二</a></p>
<p><a style="text-decoration: underline;" href="https://www.cnblogs.com/jin-xin/articles/9439483.html" target="_blank">Python最详细，最深入的代码块小数据池剖析</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/7738630.html" target="_blank">python集合,深浅copy</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8183203.html" target="_blank">python文件操作</a></p>
<h4 style="background-color: #f08080;">python函数部分</h4>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8241942.html" target="_blank">python函数初识</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8259929.html" target="_blank">python函数进阶</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8305011.html" target="_blank">python装饰器</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8423526.html" target="_blank">python迭代器,生成器</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8423937.html" target="_blank">python内置函数,匿名函数</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8743408.html" target="_blank">python递归函数</a></p>
<p><a style="text-decoration: underline;" href="https://www.cnblogs.com/jin-xin/articles/8743595.html" target="_blank">python二分查找算法</a></p>
'''
# 1,找到所有的p标签
# print()
import sys,os
# print(sys.version)

# print(os.getcwd())
# os.makedirs('abc/cbd')
# print(os.stat('/Users/baiduren/Desktop/python_code/day07-模块/test.py'))

# import time
# ft = time.strftime('%Y/%m/%d %H:%M:%S')
# st = time.strptime(ft,'%Y/%m/%d %H:%M:%S')
# print(st)
#
# t = time.mktime(st)
# print(t)
#
# t = time.time()
# st = time.localtime(t)
# print(st)
#
# ft = time.strftime('%Y/%m/%d %H:%M:%S',st)
# print(ft)

# ------------------------------- 景女神原创,张开整理 ----------------------------------
# import re
#
#
# def cal_mini_exp(mini):
#     '''
#     乘除计算
#     '''
#     if '*' in mini:
#         val1, val2 = mini.split('*')
#         return str(float(val1) * float(val2))  # 为了后面的替换，在这里把int转为str
#     elif '/' in mini:
#         val1, val2 = mini.split('/')
#         return str(float(val1) / float(val2))
#
# def dealwith(exp):
#     '''
#     整理表达式内的符号
#     '''
#     return exp.replace('--', '+').replace('+-', '-').replace('-+', '-').replace('++', '+')
#
# def calculate(son_exp):
#     '''
#         计算没有括号的表达式
#     '''
#     son_exp = son_exp.strip('()')
#     while 1:  # 完成了表达式中乘除法的计算
#         ret = re.search('\d+\.?\d*[*/]-?\d+\.?\d*', son_exp)
#         if ret:
#             mini_exp = ret.group()
#             res = cal_mini_exp(mini_exp)  # 乘除计算结果并返回结果
#             son_exp = son_exp.replace(mini_exp, res, 1)
#         else:
#             break
#     son_exp = dealwith(son_exp)  # 整理那些加加减减去重 3-+1--2之类的
#     # 最后的加减法计算
#     res = re.findall('[+-]?\d+\.?\d*', son_exp)
#     sum = 0
#     for i in res:
#         sum += float(i)
#     return str(sum)
#
#
# def remove_bracket(express):
#     '''
#     去括号
#     把内部不再有小括号的表达式匹配出来   :\([^()]+\)
#     '''
#     while 1:
#         ret = re.search('\([^()]+\)', express)  # 是否匹配上的对象
#         if ret:
#             son_exp = ret.group()  # 子表达式
#             # 计算，先乘除后加减
#             ret = calculate(son_exp)
#             express = express.replace(son_exp, ret, 1)
#         else:
#             break
#     return express
#
# def main(express):
#     express = express.replace(' ', '')  # 首先是去空格
#     express = remove_bracket(express)
#     ret = calculate(express)
#     return ret
#
# def core():
#     print('输入计算的内容或输入Q退出'.center(30, '*'))
#     while 1:
#         express = '-1 + 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
#         # express = input('please enter: ')
#         # express = '1 + 1'
#         if express == 'Q' or express == 'q':
#             break
#         elif '/0' in express:
#             print('0不能为被除数')
#         elif express.count('(') != express.count(')') or '=' in express:
#             print('表达式错误，请重新输入')
#         else:
#             ret = main(express)
#             print('计算结果：', ret)
#             break
#     print('eval计算结果: ', eval(express))
#
#
# if __name__ == '__main__':
#     core()

# import re
# exp = '-1 + 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'.replace(' ', '')
# # print(exp)  # -1+2*(3-(-4*3)/(16-3*2))
#
# def foo2(exp):
#     ''' 只计算最小的乘除单位 3/2     2*3 '''
#     if '/' in exp:
#         r1, r2 = exp.split('/')
#         return str(float(r1) / float(r2))
#     if '*' in exp:
#         r3, r4 = exp.split('*')
#         return str(float(r3) * float(r4))
# def foo1(exp):
#     ''' 去括号，然后匹配出最小的算式，包括乘除，最后再算加减 '''
#     exp = exp.strip('()')       # 9-2*5/3+7/3*99/4*2998+10*568/14
#     while 1:
#         ret = re.search('\d+\.?\d*[*/]\d+\.?\d*', exp)  # 匹配最小的乘除算式10*568
#
#         if ret:
#             r1 = ret.group()
#             r2 = foo2(r1)   # 接收计算结果
#             # print(r1, r2)
#             exp = exp.replace(r1, r2, 1)
#         else:
#             break
#     print(2222222222, exp)
#     exp = exp.replace('+-', '-').replace('-+', '-').replace('++', '+').replace('--', '+')
#     # 计算加减算式的过程
#     res = re.findall('[+-]?\d+\.?\d*', exp)
#     sum = 0
#     for i in res:
#         sum += float(i)
#     return str(sum)
#
# while 1:
#     ret = re.search('\([^()]+\)', exp)
#     if ret:
#         r1 = ret.group()
#         # print(r1)
#         r2 = foo1(r1)
#         # print(r1, r2)
#         exp = exp.replace(r1, r2, 1)
#     else:
#         break
# '''
# -1+2*60-30-72.0-3.3333333333333335+7/3*99/4*2998+10*568/14+12.0/16-6.0
#
# -1+120.0-30-72.0-3.3333333333333335+7/3*99/4*2998+10*568/14+12.0/16-6.0
#
# # 接下来，我们要做的
# 1. 要计算并替换所有的乘除，-1+120.0-30-72.0-3.3333333333333335+7/3*99/4*2998+10*568/14+12.0/16-6.0
# 2. 要把第一步的结果，再去加减算出来，-1+120.0-30-72.0-3.3333333333333335+7
# 3. 经过上两步后，得出最终结果 -1+120.0 = 119
# 4. 整理
#
# 计算器整体思路：
# 准备工作：
#     1. 检验该算式是否合法？
#         -- 有没有除数为0的 : 3 /0
#         -- 括号是不是成对的？
#     2. 应该是交互的
#         -- 用户可以输入算式，
#         -- 调用第1步去校验算式
#     3. 把功能拆分为函数，并把所有的代码封装到函数中
#
# 开始：
#     1. 拿到一个算式，并去算式的空格，方便以后处理
#     2. 用正则匹配算式中最小的括号，该循环去循环
#     3. 拿到最小的括号之后，(9-2*5/3+7/3*99/4*2998+10*568/14)
#     4. 去括号，9-2*5/3+7/3*99/4*2998+10*568/14
#     5. 再用正则去匹配算式 9-2*5/3+7/3*99/4*2998+10*568/14 中的最小的乘除单位 2*5
#     6. 拿到最小的乘除单位之后，2*5， 去计算该算式并求出结果，
#     7. 拿到上一步计算的结果后，将该结果替换道原来的算式中 9-10/3+7/3*99/4*2998+10*568/14
#     8. 整理 +- -- ++ -+
#     9. 整理完成后，得出：-1+120.0-30-72.0，到这一步，已经算完乘除，整理完+-之类的了
#     10. 计算第9步中的加减算式
#     11. 得出最终结果。

# '''
# exp = foo1(exp)
# print(exp)
#
# print(eval(exp))






# def cal_mini_exp(mini):
#     '''
#     乘除计算
#     :param mini:
#     :return:
#     '''
#     if '*' in mini:
#         val1, val2 = mini.split('*')
#         return str(float(val1) * float(val2))  # 为了后面的替换，在这里把int转为str
#     elif '/' in mini:
#         val1, val2 = mini.split('/')
#         return str(float(val1) / float(val2))
#
#
# def dealwith(exp):
#     '''
#     整理表达式内的符号
#     :param exp:
#     :return:
#     '''
#     # exp = exp.replace('--', '+')
#     # exp = exp.replace('+-', '-')
#     # exp = exp.replace('+-', '-')
#     # exp = exp.replace('++', '+')
#     exp = exp.replace('--', '+').replace('+-', '-').replace('-+', '-').replace('++', '+')
#     # print(exp)
#     return exp
#

# def calculate(son_exp):
#     '''
#         计算没有括号的表达式
#     :return:
#     '''
#     son_exp = son_exp.strip('()')
#     while 1:  # 完成了表达式中乘除法的计算
#
#         ret = re.search('\d+\.?\d*[*/]-?\d+\.?\d*', son_exp)
#         if ret:
#             mini_exp = ret.group()
#             res = cal_mini_exp(mini_exp)  # 乘除计算结果并返回结果
#             son_exp = son_exp.replace(mini_exp, res, 1)
#         else:
#             break
#     son_exp = dealwith(son_exp)  # 整理那些加加减减去重 3-+1--2之类的
#     # print(44444444, son_exp)
#     # 最后的加减法计算
#     res = re.findall('[+-]?\d+\.?\d*', son_exp)
#     # print(55555555, res)
#     sum = 0
#     for i in res:
#         sum += float(i)
#         # print(sum)
#     return str(sum)
#
#
# def remove_bracket(express):
#     '''
#     去括号
#     把内部不再有小括号的表达式匹配出来   :\([^()]+\)
#     :return:
#     '''
#     while 1:
#         ret = re.search('\([^()]+\)', express)  # 是否匹配上的对象
#         if ret:
#             son_exp = ret.group()  # 子表达式
#             # print(son_exp)  # (-40/5)
#             # 计算，先乘除后加减
#             ret = calculate(son_exp)
#             # print(ret)
#             express = express.replace(son_exp, ret, 1)
#         else:
#             break
#     return express
#
# def main(express):
#     express = express.replace(' ', '')  # 首先是去空格
#     express = remove_bracket(express)
#     # print(111, express)
#     ret = calculate(express)
#     print('计算结果：', ret)
#
# if __name__ == '__main__':
#     print('输入计算的内容或输入Q退出'.center(30, '*'))
#     while 1:
#         # express = '-1 + 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
#
#         express = input('please enter: ')
#         # express = '1 + 1'
#         if express == 'Q' or express == 'q':
#             break
#         elif '/0' in express:
#             print('0不能为被除数')
#         elif express.count('(') != express.count(')') or '=' in express:
#
#             print('表达式错误，请重新输入')
#         else:
#             main(express)
#             # break
    # print(eval(express))