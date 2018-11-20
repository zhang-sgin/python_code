# class Foo:
#     def __init__(self):
#         pass
#     def __call__(self, *args, **kwargs):
#         print(args)
#         print('__call__')
# obj = Foo()
# obj('WuSir', 'alex')  # 对象() 触发 __call__()方法


class A:

    name = 'alex'
    def __init__(self):
        pass

    def func(self):
        print('IN func')

print(getattr(A, 'name'))
# ret = getattr(A, 'func')
# ret(1)
# ret = input('>>>>')  # 'func'
# f1 = getattr(A, ret)(1)




class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#
obj = A('脸哥', 27)


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
