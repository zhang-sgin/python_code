'''
1. 用户先给自己的账户充钱：比如先充3000元。
2. 页面显示 序号 + 商品名称 + 商品价格，如：
	1 电脑 1999
	2 鼠标 10
	…
	n 购物车结算
3. 用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车，用户还可继续添加商品。
4. 如果用户输入的商品序号有误，则提示输入有误，并重新输入。
5. 用户输入n为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，则让用户删除某商品，直至可以购买，若充值的钱数充足，则可以直接购买。
6. 用户输入Q或者q退出程序。
7. 退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少。
'''

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
        print(i, dic[i]["name"]+' '+dic[i]["price"])
    print('输入n或N进行结算'
          '输入Q或q退出程序(如不结算购物车可直接退出)')
    chooise = input('有如上商品想要点啥？').strip()
    if chooise.isdigit():
        chooise = int(chooise)
        if 0 < chooise <= len(dic):
            if chooise == 1:
                account1+=1
                print('您选择的商品信息：商品名称：电脑，商品价格：1999商品数量：{}，并成功添加到购物车中。'\
                  .format(account1))
            elif chooise == 2:
                account2+=1
                print('您选择的商品信息：商品名称：鼠标，商品价格：100 商品数量：{}，并成功添加到购物车中。'\
                  .format(account2))
            elif chooise == 3:
                account3+=1
                print('您选择的商品信息：商品名称：键盘，商品价格：500 商品数量：{}，并成功添加到购物车中。'\
                  .format(account3))
            elif chooise == 4:
                account4+=1
                print('您选择的商品信息：商品名称：手机，商品价格：5000 商品数量：{}，并成功添加到购物车中。'\
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
              '您选择的商品信息：商品名称：手机，商品价格：5000 商品数量：{}。'''\
              .format(account1,account2,account3,account4))
            if all_price <= money:
                print('消费成功，您的账单总金额为{},账户余额{},欢迎下次光临！'.format(all_price,money-all_price))
                break
            while all_price > money:
                del_option = input('金额不足，请放下一些东西吧！')
                all_price = all_price - int(dic[del_option]["price"])
                if all_price <= money:
                    print('消费成功，您的账单总金额为{},账户余额{},欢迎下次光临！'.format(all_price, money - all_price))
    elif chooise.upper() == 'Q':
        print('您本次消费金额为{}元，剩余金额为{}元'.format(all_price,money-all_price))
        break
    else:
        print('-------------您的输入有误，请重新输入---------------------')