'''
1.有变量name = "aleX leNb" 完成如下操作：
		1)  移除 name 变量对应的值两边的空格,并输出处理结果
		2)  移除name变量左边的"al"并输出处理结果
		3)  移除name变量右面的"Nb",并输出处理结果
		4)  移除name变量开头的a"与最后的"b",并输出处理结果
		5)  判断 name 变量是否以 "al" 开头,并输出结果
		6)  判断name变量是否以"Nb"结尾,并输出结果
		7)  将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
		8)  将name变量对应的值中的第一个"l"替换成"p",并输出结果
		9)  将 name 变量对应的值根据 所有的"l" 分割,并输出结果。
		10) 将name变量对应的值根据第一个"l"分割,并输出结果。
		11) 将 name 变量对应的值变大写,并输出结果
		12) 将 name 变量对应的值变小写,并输出结果
		13) 将name变量对应的值首字母"a"大写,并输出结果
		14) 判断name变量对应的值字母"l"出现几次，并输出结果
		15) 如果判断name变量对应的值前四位"l"出现几次,并输出结果
		16) 从name变量对应的值中找到"N"对应的索引(如果找不到则报错)，并输出结果
		17) 从name变量对应的值中找到"N"对应的索引(如果找不到则返回-1)输出结果
		18) 从name变量对应的值中找到"X le"对应的索引,并输出结果
		19) 请输出 name 变量对应的值的第 2 个字符?
		20) 请输出 name 变量对应的值的前 3 个字符?
		21) 请输出 name 变量对应的值的后 2 个字符?
		22) 请输出 name 变量对应的值中 "e" 所在索引位置?
'''
# name = "aleX leNb"
'''1-5'''
# print(name.strip())
# print(name.lstrip('al'))
# print(name.rstrip('Nb'))
# print(name.strip('a/b'))
# print(name.startswith('al'))
'''6-10'''
# print(name.endswith('Nb'))
# print(name.replace('l','p'))
# print(name.replace('l','p',1))
# print(name.split('l'))
# print(name.split('l',1))
'''11-15'''
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.count('l'))
# print(name.count('l',4))
'''16-28'''
# print(name.index('N'))
# print(name.find('N'))
# print(name.index('X le'))
# name19 = name [2]
# print(name19)
# name20 = name[:3]
# print(name20)
# name21 = name[-1:-3:-1]
# print(name21)
# print(name.find('e'))

'''
2、有字符串s = "123a4b5c"
        1)通过对s切片形成新的字符串s1,s1 = "123"
		2)通过对s切片形成新的字符串s2,s2 = "a4b"
		3)通过对s切片形成新的字符串s3,s3 = "1345"
		4)通过对s切片形成字符串s4,s4 = "2ab"
		5)通过对s切片形成字符串s5,s5 = "c"
		6)通过对s切片形成字符串s6,s6 = "ba2"
'''
s = "123a4b5c"
# s1 = s [:3]
# print(s1)
# s2 = s [3:6]
# print(s2)
# s3 = s [::2]
# print(s3)
# s4 = s [1:6:2]
# print(s4)
# s5 = s [-1]
# print(s5)
# s6 = s [-3:-8:-2]
# print(s6)

'''
3、使用while或for循环分别打印字符串s="asdfer"中每个元素。
'''
# s="asdfer"
# for i in s:
#     print(i)

'''
4、使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"
'''
# s="asdfer"
# for i in s:
#     print(s)

'''
5、使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字符加上sb， 例如：asb, bsb，csb,...gsb。
'''
# s="asdfer"
# for i in s:
#     print(i+'sb')

'''
6、使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
'''
# s = "321"
# for i  in s:
#     msg = "倒计时" +i +"秒"
#     print(msg)
# print("出发！")
'''
7、实现一个整数加法计算器(两个数相加)：
	如：content = input("请输入内容:") 用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。
'''
# content = input("请输入内容:").strip()
# ist = content.split('+')
# jj=0
# for i in ist:
#     jj+=int(i)
# print(jj)
'''
8、升级题：实现一个整数加法计算器（多个数相加）：
	如：content = input("请输入内容:") 用户输入：5+9+6 +12+  13，然后进行分割再进行计算。
'''
# content = input("请输入内容:").strip()
# ist = content.split('+')
# jj=0
# for i in ist:
#     jj+=int(i)
# print(jj)

'''
9、计算用户输入的内容中有几个整数（以个位数为单位）。
	ntent = input("请输入内容：")   # fhdal234slfh98769fjdla
'''
# ntent = input("请输入内容：")
# jj = 0
# for i in ntent:
#     if i.isdigit():
#         jj+=1
# print(jj)
'''
10.	10、写代码，完成下列需求：
    用 户可持续输入（用while循环），用户使用的情况：
    输入A，则显示走大路回家，然后在让用户进一步选择： 是选择公交车，还是步行？
    选择公交车，显示10分钟到家，并退出整个程序。
    选择步行，显示20分钟到家，并退出整个程序。
    输入B，则显示走小路回家，并退出整个程序。
    输入C，则显示绕道回家，然后在让用户进一步选择：是选择游戏厅玩会，还是网吧？
    选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
    选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。
'''

'''
11、写代码：计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和？
'''
# cont = 0
# for i in range(1,100):
#     if i ==88:
#         continue
#     elif i%2==0:
#         cont -= i
#     else:
#         cont += i
# print(cont)

'''
16、制作趣味模板程序需求：等待⽤户输⼊名字、地点、爱好，根据⽤户的名字和爱好进⾏任意现实       
	如：敬爱可亲的xxx，最喜欢在xxx地⽅⼲xxx
'''
# name = input('请输入姓名：')
# di = input('请输入地点：')
# hobby = input('请输入爱好：')
# msg = """敬爱可亲的%s，最喜欢在%s地方%s""" % (name,di,hobby)
# print(msg)

'''
17、等待⽤户输⼊内容，检测⽤户输⼊内容中是否包含敏感字符？
如果存在敏感字符提示“存在敏感字符请重新输⼊”，并允许⽤户重新输⼊并打印。敏感字符：“⼩粉嫩”、“⼤铁锤”
'''
# min = ["小粉嫩","大铁锤"]
# for i in min:
#     sou = input('请输入搜索内容：')
#     if sou not in min:
#         print("ojbk")
#         break
#     else:
#         print("您输入的内容包含敏感字符，请重新输入！")
