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
        return  str(float(num1)*float(num2))
    elif '/' in small:
        num1,num2 = small.split('/')
        return  str(float(num1)/float(num2))

def trim(exp):
    exp = exp.replace('--','+')
    exp = exp.replace('+-','-')
    exp = exp.replace('-+','-')
    exp = exp.replace('++','+')
    return exp
    

def wipe(son_keng):
    son_keng = son_keng.strip('()')
    ret = re.search('\d+\.?\d*[*/]-?\d+\.?\d*', son_keng)
    while 1:
        if ret:
            small_keng = ret.group()
            res = count_small_keng(small_keng)  # 乘除计算结果并返回结果
            son_keng = son_keng.replace(small_keng, res,1)
        else:
            break
    son_keng = trim(son_keng)
    ret_list = re.findall('[+-]?\d+\.?\d*',son_keng)
    sum = 0
    for i in ret_list:
        sum += float(i)
    return str(sum)

    
keng = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )".replace(' ','')
while 1:
    zz = re.search('\([^()]+\)', keng)
    if zz:
        son_keng = zz.group()
        zz = wipe(son_keng)
        keng = keng.replace(son_keng,zz,1)
    else:
        break
    
print('-----结果是：',keng)