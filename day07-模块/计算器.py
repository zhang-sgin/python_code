

def cal_mini_exp(mini):
    if '*' in mini:
        val1, val2 = mini.split('*')
        return str(float(val1) * float(val2))  # 为了后面的替换，在这里把int转为str
    elif '/' in mini:
        val1, val2 = mini.split('/')
        return str(float(val1) / float(val2))


def dealwith(exp):
    exp = exp.replace('--', '+').replace('+-', '-').replace('-+', '-').replace('++', '+')
    return exp


def calculate(son_exp):
    son_exp = son_exp.strip('()')
    while 1:  # 完成了表达式中乘除法的计算
        ret = re.search('\d+\.?\d*[*/]-?\d+\.?\d*', son_exp)
        if ret:
            mini_exp = ret.group()
            res = cal_mini_exp(mini_exp)  # 乘除计算结果并返回结果
            son_exp = son_exp.replace(mini_exp, res, 1)
        else:
            break
    son_exp = dealwith(son_exp)  # 整理那些加加减减去重 3-+1--2之类的
    res = re.findall('[+-]?\d+\.?\d*', son_exp)
    sum = 0
    for i in res:
        sum += float(i)
        # print(sum)
    return str(sum)


def remove_bracket(express):
    while 1:
        ret = re.search('\([^()]+\)', express)  # 是否匹配上的对象
        if ret:
            son_exp = ret.group()  # 子表达式
            ret = calculate(son_exp)
            express = express.replace(son_exp, ret, 1)
        else:
            break
    return express

def main(express):
    express = express.replace(' ', '')  # 首先是去空格
    express = remove_bracket(express)
    ret = calculate(express)
    print('计算结果：', ret)

if __name__ == '__main__':
    print('输入计算的内容或输入Q退出'.center(30, '*'))
    while 1:
        # express = '-1 + 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

        express = input('please enter: ')
        # express = '1 + 1'
        if express == 'Q' or express == 'q':
            break
        elif '/0' in express:
            print('0不能为被除数')
        elif express.count('(') != express.count(')') or '=' in express:

            print('表达式错误，请重新输入')
        else:
            main(express)
            # break
    print(eval(express))