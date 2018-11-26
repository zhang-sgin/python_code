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