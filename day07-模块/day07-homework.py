'''
作业：计算器
	实现加减乘除及拓号优先级解析
	用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式
	注意：不能调用eval等类似功能偷懒实现
'''
import re

def count_small_keng(small):
    if '*' in small:
        num1,num2 = small.split('*')
        return  str(float(num1) * float(num2))
    elif '/' in small:
        num1,num2 = small.split('/')
        return  str(float(num1) / float(num2))

def trim(exp):
    exp = exp.replace('--', '+').replace('+-', '-').replace('-+', '-').replace('++', '+')
    return exp
    

def wipe(son_keng):
    son_keng = son_keng.strip('()')
    while True:
        ret = re.search('\d+\.?\d*[*/]-?\d+\.?\d*', son_keng)
        if ret:
            small_keng = ret.group()
            res = count_small_keng(small_keng)
            son_keng = son_keng.replace(small_keng, res, 1)
        else:
            break
    son_keng = trim(son_keng)
    res = re.findall('[+-]?\d+\.?\d*', son_keng)
    sum = 0
    for i in res:
        sum += float(i)
    return str(sum)

def re_bracket(keng):
    while True:
        zz = re.search('\([^()]+\)', keng)
        if zz:
            son_keng = zz.group()  # 子表达式
            zz = wipe(son_keng)
            keng = keng.replace(son_keng, zz, 1)
        else:
            break
    return keng

def main(keng):
    keng = keng.replace(' ','')
    keng = re_bracket(keng)
    ret = wipe(keng)
    print('计算结果：',ret)

# if __name__ == '__main__':
#     keng = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
#     main(keng)

if __name__ == '__main__':
    print('输入计算的内容或输入Q退出'.center(30, '*'))
    while True:
        keng = input('please enter: ')
        if keng == 'Q' or keng == 'q':
            break
        elif '/0' in keng:
            print('0不能为被除数')
        else:
            main(keng)
    # print(eval(keng))


# 任务停在第一个-40/8这里无限循环，早上查一下为什么循环不往下走