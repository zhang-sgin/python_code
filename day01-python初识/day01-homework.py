'''
⽤户登录
1. 三次重试机会
2. 每次输错误时显⽰剩余错误次数
'''

#一：
error = 0
while error <= 3:
    error += 1
    name = input('请输入用户名： ')
    pwd = input('请输入用户名密码： ')
    pwd = int(pwd)
    if name == 'zz':
        if pwd == 123:
            print('登录成功')
            break
        else:
            print('密码错误，请重试')
            if error == 1:
                print('失败第一次，还剩下两次机会')
            elif error == 2:
                print('失败第二次，还剩一次机会')
            elif error == 3:
                print('今日已失败三次，明天请早')
                break
    else:
        print('用户名错误，请重试')
        if error == 1:
            print('失败第一次，还剩下两次机会')
        elif error == 2:
            print('失败第二次，还剩一次机会')
        elif error == 3:
            print('今日已失败三次，明天请早')
            break

#二：
name = 'zz'
pwd = 123
error = 0
while error < 3:
    error = error + 1
    in_name = input('请输入用户名： ')
    in_pwd = input('请输入用户名密码： ')
    pwd = int(pwd)
    if in_name == name and in_pwd == pwd:
        print('恭喜，登录成功')
        break
    else:
        print('登录失败，请重试')
        if error == 1:
            print('失败第一次，还剩下两次机会')
        elif error == 2:
            print('失败第二次，还剩下一次')
        elif error == 3:
            print('今日已失败三次，明天请早')
            break

