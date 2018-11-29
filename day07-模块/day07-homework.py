'''
作业：计算器
	实现加减乘除及拓号优先级解析
	用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式
	注意：不能调用eval等类似功能偷懒实现
'''
import re

#乘除法计算函数
def count_small_keng(small):
    if '*' in small:
        num1,num2 = small.split('*')
        return  str(float(num1) * float(num2))
    elif '/' in small:
        num1,num2 = small.split('/')
        return  str(float(num1) / float(num2))

#处理多符号函数
def trim(exp):
    exp = exp.replace('--', '+').replace('+-', '-').replace('-+', '-').replace('++', '+')
    return exp
    

def wipe(son_keng):
    son_keng = son_keng.strip('()') # 去除子表达式两边的空格 (-40/5) 变成-40/5
    while True:
        ret = re.search('\d+\.?\d*[*/]-?\d+\.?\d*', son_keng)   # 从传进来的公式中，取出 （整数/小数 '\d+\.?\d*'） [*/] （负数/整数/小数   '-?\d+\.?\d*'）,被乘数和被除数如果是负数，不去- ，例如：-40/5 只取40/5，结果等8 加上-，等于-8
        if ret: # 如果取出了
            small_keng = ret.group()    # small_keng = 40/5
            res = count_small_keng(small_keng)  # 执行count_small_keng函数 乘除法计算 结果赋值给res
            son_keng = son_keng.replace(small_keng, res, 1) # 将son_keng传进来的公式替换成res的值
        else:
            break
    son_keng = trim(son_keng)    #执行trim函数，处理多个运算符
    res = re.findall('[+-]?\d+\.?\d*', son_keng)    # 计算加减法  匹配规则 [+-]（/整数/小数   '?\d+\.?\d*'） 例如40+30  为40和+30
    sum = 0
    for i in res:
        sum += float(i)
    return str(sum)


def re_bracket(keng):
    while True:
        zz = re.search('\([^()]+\)', keng) # 取出公式最里面括号内的计算公式
        if zz:  # 如果取出了
            son_keng = zz.group()  # 子表达式 (-40/5)
            zz = wipe(son_keng)   #执行wipe函数，计算子表达式的值
            keng = keng.replace(son_keng, zz, 1)   # 讲wipe计算完的数值替换进用户输入的公式中
        else:
            break
    return keng


def main(keng):
    keng = keng.replace(' ','') # 去除公式空格 1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
    keng = re_bracket(keng) # 执行re_bracket函数，取出公式最里面括号内的计算公式
    ret = wipe(keng)    #打印结果
    print('计算结果：',ret)


if __name__ == '__main__':
    print('输入计算的内容或输入Q退出'.center(30, '*'))
    while True:
        keng = input('请输入计算内容: ')  # 输入计算的公式   1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
        if keng == 'Q' or keng == 'q':  # 如果Q推出程序
            break
        elif '/0' in keng:  # 如果/0在公式中，提示0不能为除数
            print('0不能为被除数')
        else:
            main(keng) #执行main函数，并且把公式传进去 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )


