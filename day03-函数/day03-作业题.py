'''
作业：用函数完成登录注册以及购物车的功能。
	1，启动程序，用户可选择四个选项：登录，注册，购物，退出。
	2，用户注册，用户名不能重复，注册成功之后，用户名密码记录到文件中。
	3，用户登录，用户名密码从文件中读取，进行三次验证，验证不成功则退出整个程序。
	4，用户登录成功之后才能选择购物功能进行购物，购物功能（就是将购物车封装到购物的函数中）。
	5，退出则是退出整个程序。
'''

'''
1.用户登录-->
2.读取用户信息文件，读取用户信息，判断输入的用户名密码是否正确-->
3.如果正确的，调用购物车-->
4.如果不正确，提示错误密码，并提示注册用户，注册后到第二步
'''

import  os
msg=('''
####################操作选项：##################
1.登录
2.注册
3.购物
4.退出
#######################GG#######################
''')
msg2=('''
####################操作选项：##################
3.购物
4.退出
#######################GG#######################
''')

def register():
    register_user_name = input('请注册您的用户名：')
    register_password = input('请注册您的用户名密码：')
    with open('user_info.txt', encoding='utf-8',mode='r+')as f_register:
        for line in f_register:
            user_info = line.split(' ')
            if register_user_name in user_info:
                print('用户已存在')
                continue
            else:
                f_register.write(register_user_name + ' ' + register_password + '\n')
                print('{}用户注册成功'.format(register_user_name))
                break

def login():
    count=1
    while count < 4:
        login_user_name=input('请输入您的用户名：')
        login_password=input('请输入用户名密码：')
        with open('user_info.txt',encoding='utf-8')as f_login:
            for i in f_login:
                login_line=i.strip().split(' ')
                if login_user_name == login_line[0] and login_password == login_line[1]:
                    print(login_line)
                    print('登录成功')
                    print(msg2)
                    caozuo_num = int(input('请输入操作选项：'))
                    if caozuo_num == 3:
                        shopping()
                    elif caozuo_num == 4:
                        print('您已退出程序')
                        quit()
                else:
                    print('用户名或密码错误，请重新输入，您还有{}次机会'.format(3 - count))
                    count+=1
                break

def shopping():
    dic = {"1":{"name":"电脑","price":"1999"},
           "2":{"name":"鼠标","price":"100"},
           "3":{"name":"键盘","price":"500"},
           "4":{"name":"手机","price":"5000"},
    }

    flag=True
    account1 =0
    account2 =0
    account3 =0
    account4 =0
    while True:
        money = input("请输入需要充值的金额：")
        if money.isdigit():
            money=int(money)
            print("您的资产：",money )
            break
        else:
            print("请输入正确金额")

    flag = True
    while flag:
        for i in dic:
            print(i, dic[i]["name"] + ' ' + dic[i]["price"])
        print('输入n或N进行结算'
              '输入Q或q退出程序(如不结算购物车可直接退出)')
        chooise = input('有如上商品想要点啥？').strip()
        if chooise.isdigit():
            chooise = int(chooise)
            if 0 < chooise <= len(dic):
                if chooise == 1:
                    account1 += 1
                    print('您选择的商品信息：商品名称：电脑，商品价格：1999商品数量：{}，并成功添加到购物车中。' \
                          .format(account1))
                elif chooise == 2:
                    account2 += 1
                    print('您选择的商品信息：商品名称：鼠标，商品价格：100 商品数量：{}，并成功添加到购物车中。' \
                          .format(account2))
                elif chooise == 3:
                    account3 += 1
                    print('您选择的商品信息：商品名称：键盘，商品价格：500 商品数量：{}，并成功添加到购物车中。' \
                          .format(account3))
                elif chooise == 4:
                    account4 += 1
                    print('您选择的商品信息：商品名称：手机，商品价格：5000 商品数量：{}，并成功添加到购物车中。' \
                          .format(account4))
            else:
                print('--------------您输入的商品序号超出范围，请重新输入！--------------------')
        elif chooise.upper() == 'N':
            print('您购物车的具体商品如下：')
            all_price = account1 * 1999 + account2 * 100 + account3 * 500 + account4 * 5000
            print('--------------------账单总金额为{}------------------'.format(all_price))
            print('''
                '您选择的商品信息：商品名称：电脑，商品价格：1999 商品数量：{}。'
                '您选择的商品信息：商品名称：鼠标，商品价格：100  商品数量：{}。'
                '您选择的商品信息：商品名称：键盘，商品价格：500  商品数量：{}。'
                '您选择的商品信息：商品名称：手机，商品价格：5000 商品数量：{}。''' \
                  .format(account1, account2, account3, account4))
            if all_price <= money:
                print('消费成功，您的账单总金额为{},账户余额{},欢迎下次光临！'.format(all_price, money - all_price))
                break
            while all_price > money:
                del_option = input('金额不足，请放下一些东西吧！')
                all_price = all_price - int(dic[del_option]["price"])
                if all_price <= money:
                    print('消费成功，您的账单总金额为{},账户余额{},欢迎下次光临！'.format(all_price, money - all_price))
        elif chooise.upper() == 'Q':
            print('您本次消费金额为{}元，剩余金额为{}元'.format(all_price, money - all_price))
            quit()
        else:
            print('-------------您的输入有误，请重新输入---------------------')


print(msg)
caozuo_num=int(input('请输入操作选项：'))
if caozuo_num == 1:
    login()
elif caozuo_num == 2:
    register()
elif caozuo_num == 3:
    login()
elif caozuo_num == 4:
    print('退出')