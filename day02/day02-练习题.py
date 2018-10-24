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
# s = "123a4b5c"
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
# content = input("整数加法计算器，请输入内容:").strip()
# ist = content.split('+')
# jj=0
# for i in ist:
#     if i.isdigit():
#         jj+=int(i)
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

# dic = {'A':{'走大路回家':{'Ag':'公交车10分钟到家','Ab': '步行20分钟到家'}},
#        'B':{'走小路回家': 0},
#        'C':{'绕道回家':{'Cy':'一个半小时到家，爸爸在家，拿棍等你。','Cb':'两个小时到家，妈妈已做好了战斗准备。'}}
# }
#
# flag = True
# while flag:
#     for i in dic:
#         print(i, list(dic[i].keys())[0])
#     chooise = input('您想怎么回家？')
#     if chooise == 'B':
#         print('快点回家')
#         flag = False
#     elif chooise == 'A':
#         dalu = input("公交车还是步行?")
#         if dalu == '公交车':
#             print(dic["A"]["走大路回家"]["Ag"])
#         elif dalu == '步行':
#             print(dic["A"]["走大路回家"]["Ab"])
#             break
#     elif chooise == 'C':
#         raodao = input("兄弟，绕道想去游戏厅还是网吧？")
#         if raodao == '游戏厅':
#             print(dic["C"]["绕道回家"]["Cy"])
#             continue
#         elif raodao == '网吧':
#             print(dic["C"]["绕道回家"]["Cb"])
#             continue

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

'''
	18、写代码，有如下列表，按照要求实现每一个功能
		li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
		1)计算列表的长度并输出
		2)列表中追加元素"seven",并输出添加后的列表
		3)请在列表的第1个位置插入元素"Tony",并输出添加后的列表
		4)请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
		5)请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
		6)请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
		7)请给列表添加元素"eric",并输出添加后的列表
		8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
		9)请删除列表中的第2至4个元素，并输出删除元素后的列表
		10)请将列表所有得元素反转，并输出反转后的列表
		11)请计算出"alex"元素在列表li中出现的次数，并输出该次数。
'''
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
'''1-5'''
#18.1
# print(len(li))
#18.2
# li.append('seven')
# print(li)
# 18.3
# li.insert(0,'Tony')
# print(li)
# 18.4
# li[1] = 'Kelly'
# print(li)
# 18.5
# li.extend(['1', 'a', '3', '4' ,'heart'])
# print(li)
# 18.6
# li.extend(('qwert'))
# print(li)
# 18.7
# li.append('eric')
# print(li)
# 18.8
# ret = li.pop(1)
# print(ret)
# print(li)
# 18.9
# del li[1::1]
# print(li)
# 18.10
# li.reverse()
# print(li)
# 18.11
# print(li.count(li))

'''
	19、写代码，有如下列表，利用切片实现每一个功能
		li = [1, 3, 2, "a", 4, "b", 5,"c"]
			1)通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
			2)通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
			3)通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
			4)通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
			5)通过对li列表的切片形成新的列表l5,l5 = ["c"]
			6)通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
'''
# li = [1, 3, 2, "a", 4, "b", 5,"c"]
# print(li[:3])
# print(li[3:6])
# print(li[::2])
# print(li[1:7:2])
# print(li[-1:])
# print(li[-3::-2])
'''
	20、写代码，有如下列表，按照要求实现每一个功能。
		lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
		1)将列表lis中的"tt"变成大写（用两种方式）。
		2)将列表中的数字3变成字符串"100"（用两种方式）。
		3)将列表中的字符串"1"变成数字101（用两种方式）。
'''
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# 1.1
# print(lis[-3])
# lis[-3][2][1][0] = lis[-3][2][1][0].upper()
# print(lis[-3][2][1][0])
# print(lis)
# 1.2


# 2.1
# lis[1] = "100"
# print(lis[1])

# 3.1
# lis[-3][2][1][2] = '101'
# print(lis[-3][2][1][2])






'''
	21、请用代码实现： 
		li = ["alex", "eric", "rain"]
		利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
'''
# li = ["alex", "eric", "rain"]
# zz = '_'.join(li)
# print(zz)
'''
	22、利用for循环和range打印出下面列表的索引。
		li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
'''
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# for i in range(len(li)):
#     print(i)
'''
	23、利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中。
'''
# zz= []
# for i in range(0,100,2):
#     zz.append(i)
# print(zz)
'''
	24、利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中。
'''
# zz=[]
# for i in range(0,50):
#     if i%3==0:
#         zz.append(i)
# print(zz)
'''
	25、利用for循环和range从100~1，倒序打印。
'''
# for i in range(100,0,-1):
#     print(i)
'''
	26、利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来。
'''
# zz=[]
# for i in range(100,9,-2):
#     if i%4==0:
#         zz.append(i)
# print(zz)

'''
	26、利用for循环和range，将1-30的数字一次添加到一个列表中，并循环这个列表，将能被3整除的数改成*。
'''
# zz=[]
# dd=0
# for i in range(30):
#     zz.append(i)
#     print(zz)
# for i in zz:
#     if i%3==0:
#         zz[dd]="*"
#     dd+=1
# print(zz)
'''
	27、查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
		li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
'''
# li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
# zz=[]
# for i in  li:
#     print(i.strip()[0]=='a'or i.strip()[0]=='A')and i.strip()[-1]=='c'
    # if (i.strip()[0]=='a'or i.strip()[0]=='A')and i.strip()[-1]=='c':
    #     zz.append(i)
# for i in zz:
#     print(i)

'''
	28、开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
		敏感词列表 li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
		则将用户输入的内容中的敏感词汇替换成等长度的*（苍老师就替换***），并添加到一个列表中；如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
'''
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# zz=[]
# haha=input('请输入评论内容：')
# for i in li:
#     if i in haha:
#         haha = haha.replace(i,"*"*len(i))
#         zz.append(haha)
# print(haha)
# print(zz)

'''
	29、有如下变量（tu是个元祖），请实现要求的功能	
		tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
			a. 讲述元祖的特性
			b. 请问tu变量中的第一个元素 "alex" 是否可被修改？
			c. 请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"
			d. 请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"
'''
tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
# a.元组被称为只读列表，数据可以被查询，但不能修改
# b.元组的数据不可修改
# c.k2对应的值是字典，是可以修改的。
# print(type(tu[1][2]["k2"]))
# tu[1][2]["k2"].append("seven")
# d.k3对应的值是元组，是不可以修改的。
# print(type(tu[1][2]["k3"]))

'''
	30、字典dic,dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
	   
		a. 请循环输出所有的key
		b. 请循环输出所有的value
		c. 请循环输出所有的key和value
		d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
		e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
		f. 请在k3对应的值中追加一个元素 44，输出修改后的字典
		g. 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
'''

'''
	31、av_catalog = {
			"欧美":{
				"www.youporn.com": ["很多免费的,世界最大的","质量一般"],
				"www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
				"letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
				"x-art.com":["质量很高,真的很高","全部收费,屌丝请绕过"]
			},
			"日韩":{
				"tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]
			},
			"大陆":{
				"1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
			}
		}

		a,给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个  元素：'量很大'。
		b,将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
		c,将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收  费,屌丝请绕过" 删除。
		d,将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
		e,给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
		f,删除此"letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]键值对。
		g,给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
'''
'''
	32、有字符串"k:1|k1:2|k2:3|k3:4" 处理成字典 {'k':1,'k1':2....}
'''
'''
	33、元素分类
		有如下值li= [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
		即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}
'''




















