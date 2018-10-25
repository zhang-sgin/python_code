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
show_dic = {}
# while True:
#     money = input("请输入需要充值的金额：")
#     if money.isdigit():
#         money=int(money)
#         print("您的资产：",money )
#         break
#     else:
#         print("请输入正确金额")

flag = True
while flag:
    for i in dic:
        print(i, dic[i]["name"]+' '+dic[i]["price"])
    print('输入Q或q进行结算\n输入Q或q退出程序(如不结算购物车可直接退出)')
    chooise = input('有如上商品想要点啥？').strip()
    if chooise.isdigit():
        chooise = int(chooise)
        if 0 < chooise <= len(dic):
            if (chooise - 1) not in show_dic:
                show_dic[chooise - 1]['amount'] += 1
            print('您选择的商品信息：商品名称：{}商品价格：{}商品数量：1，并成功添加到购物车中。' \
                  .format(dic[chooise]['name'], dic[chooise - 1]['price']))
        else:
            print('您输入的序号超出范围，请重新输入：')









# flag=True
# dic = [{"name":"电脑","price":1999},
#        {"name":"鼠标","price":100},
#        {"name":"键盘","price":500},
#        {"name":"手机","price":5000},
# ]
# print(dic)

