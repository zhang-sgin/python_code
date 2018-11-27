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
    while 1:
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

def day07(keng):
    while 1:
        zz = re.search('\([^()]+\)', keng)
        if zz:
            son_keng = zz.group()  # 子表达式
            zz = wipe(son_keng)
            express = keng.replace(son_keng, zz, 1)
        else:
            break
    return keng

def main(keng):
    keng = keng.replace(' ','')
    keng = day07(keng)
    ret = wipe(keng)
    print('计算结果：',ret)

# if __name__ == '__main__':
#     keng = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
#     main(keng)

if __name__ == '__main__':
    print('输入计算的内容或输入Q退出'.center(30, '*'))
    while 1:
        keng = input('please enter: ')
        if keng == 'Q' or keng == 'q':
            break
        elif '/0' in keng:
            print('0不能为被除数')
        elif keng.count('(') != keng.count(')') or '=' in keng:

            print('表达式错误，请重新输入')
        else:
            main(keng)
    print(eval(keng))