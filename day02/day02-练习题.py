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
name = "aleX leNb"
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
