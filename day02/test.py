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

dic = {"1":["name":"电脑","price":"1999"],
       "2":["name":"鼠标","price":"100"],
       "3":["name":"键盘","price":"500"],
       "4":["name":"手机","price":"5000"],
}
flag=True
show_dic = {}
while True:
    money = input("请输入需要充值的金额：")
    if money.isdigit():
        money=int(money)
        print("已充值金额：",money )
        break
    else:
        print("请重新输入金额")

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
                show_dic[chooise -1] = {'name':"电脑", 'price': 1999, 'amount': 1}
                print('您选择的商品信息：商品名称：{}，商品价格：{}商品数量：1，并成功添加到购物车中。'\
                  .format("电脑", 1999))
            elif chooise == 2:
                show_dic[chooise -1] = {'name':"鼠标", 'price': 100, 'amount': 1}
                print('您选择的商品信息：商品名称：{}，商品价格：{}商品数量：1，并成功添加到购物车中。'\
                  .format("鼠标", 100))
            elif chooise == 3:
                show_dic[chooise -1] = {'name':"键盘", 'price': 500, 'amount': 1}
                print('您选择的商品信息：商品名称：{}，商品价格：{}商品数量：1，并成功添加到购物车中。'\
                  .format("键盘", 500))
            elif chooise == 4:
                show_dic[chooise -1] = {'name':"手机", 'price': 5000, 'amount': 1}
                print('您选择的商品信息：商品名称：{}，商品价格：{}商品数量：1，并成功添加到购物车中。'\
                  .format("手机", 5000))
        else:
            print('--------------您输入的商品序号超出范围，请重新输入！--------------------')
    elif chooise.upper() == 'N':
        while True:
            print('您购物车的具体商品如下：')
            all_price = 0
            for k, v in show_dic.items():
                print('序号：{}商品名称{}商品单价{}此商品总价：{}' \
                      .format(k + 1, v['name'], v['price'], v['price'] * v['amount']))
                all_price += v['price'] * v['amount']
            print('————————> 总价格：%s元' % all_price)
            if money >= all_price:
                money=int(money)
                print('购买成功，还剩%s元，欢迎下次光临！' % money)
                break
            else:
                print('兄弟，还差%s元，放下一些东西吧！' % (all_price  - money))
            del_num = input('放下一些东西吧：').strip()
            if del_num.isdigit():
                if (del_num - 1) in show_dic:
                    show_dic[del_num -1 ]['account'] -= 1
                    if not show_dic[del_num -1]['account']:
                        del show_dic[del_num - 1]
                else:
                    print('输入序号有误，请重新输入：')
            else:
                print('输入序号有误，请重新输入：')
    elif chooise.upper() == 'Q':
        print('再见，欢迎下次光临！')
        break
    else:
        print('-------------您的输入有误，请重新输入---------------------')