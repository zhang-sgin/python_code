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


import random
from time import sleep

# 所有涉及金额的浮点数都需要用 round 方法保留2位小数，避免出现最终结果多出0.01
amount = round(float(input('请设置红包的金额 \> ')), 2)
num = int(input('请设置红包的数量 \> '))
hb_dict = {}
xing = '赵钱孙李周吴郑王'
ming = '一二三四五六七八九十'

while num:

    xingming = random.choice(xing) + random.choice(ming) + random.choice(ming)
    if xingming in hb_dict.keys():
        xingming = random.choice(xing) + random.choice(ming) + random.choice(ming)

    num -= 1
    if num == 0:
        print('%s抢到红包%.2f元 红包抢完了!' % (xingming, amount))
        hb_dict[amount] = xingming
        amount -= amount
    elif num > 0:
        hb = round(random.uniform(0.01, amount) / num, 2)
        hb_dict[hb] = xingming
        # 算法: 在0.01到红包总金额之间随机一个浮点数 / 红包剩余个数
        print('%s抢到红包%.2f元 剩余%d个!' % (xingming, hb, num))
        amount = round((amount - hb), 2)

    sleep(1)

# 转置字典中的 key / value
# hb_dict2 = {value:key for key,value in hb_dict.items()}
max_hb = max(hb_dict.items())
print('%s运气最佳 抢得%.2f元!!' % (max_hb[1], max_hb[0]))