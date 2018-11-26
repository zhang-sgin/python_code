# class Foo:
#     def __init__(self):
#         pass
#     def __call__(self, *args, **kwargs):
#         print(args)
#         print('__call__')
# obj = Foo()
# obj('WuSir', 'alex')  # 对象() 触发 __call__()方法


# class A:
#
#     name = 'alex'
#     def __init__(self):
#         pass
#
#     def func(self):
#         print('IN func')

# print(getattr(A, 'name'))
# ret = getattr(A, 'func')
# ret(1)
# ret = input('>>>>')  # 'func'
# f1 = getattr(A, ret)(1)


#
#
# class A:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# #
# obj = A('脸哥', 27)


# ret = getattr(obj, 'name', None)
# print(hasattr(obj, 'age'))
# print(ret)
# if hasattr(obj, 'name'):
#     ret = getattr(obj, 'name')
#
# setattr(obj, 'sex', '男')  # 设置
# print(getattr(obj, 'sex'))
#
# delattr(obj, 'name')  # 删除
# print(obj.__dict__)


import random
from time import sleep

#
# 第一种：
# 课程
# 语文|数学|英语
#
# 讲师
# zc|123|1班
# q|123|2班
#
# 用户：
# admin|123|123
# zz|123|member
#
#
# 班级
# 7、查看班级中的学生
# 4、为学生指定班级
# {"1班": ["zz", "zc"], "2班": ["hha", "xx", "sb"]}
#
#
# 学员选了哪些课
# {"z": ["数学", "语文", "英语", "linux", "python", "语文"], "cz": ["英语", "语文", "语文"]}
#
#
# 第二种：
# 课程
# 语文|数学|英语
#
# 用户：
# admin|123|admin
# zz|123|member
# aa|123|teacher
#
# 查看讲师带了哪些班级
# {"aa": ["1班", "2班"]}
#
#
# 班级
# 7、查看班级中的学生
# 4、为学生指定班级
# {"1班": ["zz", "zc"], "2班": ["hha", "xx", "sb"]}
#
#
# 学员选了哪些课
# {"z": ["数学", "语文", "英语", "linux", "python", "语文"], "cz": ["英语", "语文", "语文"]}
#
#
# # 1、创建讲师
# 2、为讲师指定班级
# # 3、创建班级
# 4、为学生指定班级
# 7、查看班级中的学生
# 6、查看所教班级
# 7、查看班级中的学生

# classroom_member={"zz": ["1班", "2班"]}
# stu_name=input('请输入名字')
# ret = classroom_member.get(stu_name)
# print(ret)

# classroom_member={"1班": ["sb"]}
# tmp = {'1': '1班', '2': '2班'}
#
# stu_name='gg'
# stu_choose_classroom = '1班'

# print(tmp[stu_choose_classroom],[stu_name])
# print(classroom_member.get(stu_choose_classroom))
# classroom_member.get(stu_choose_classroom).append(stu_name)
# classroom_member.get(tmp[stu_choose_classroom]).append(stu_name)
# classroom_member.setdefault(tmp[stu_choose_classroom], [stu_name])
# print(classroom_member)


print('from the tbjx.py')

__all__ = ['name', 'read1', ]

name = '太白金星'


def read1():
    print('tbjx模块：', name)


def read2():
    print('tbjx模块')
    read1()


def change():
    global name
    name = 'barry'


if __name__ == '__main__':
    # 在模块文件中测试read1()函数
    # 此模块被导入时 __name__ == tbjx 所以不执行
    read1()

