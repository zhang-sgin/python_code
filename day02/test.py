goods = [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998},
         ]
goods_car = {}
while 1:
    money = input('请输入充值的钱数：').strip()
    if money.isdigit():
        money = int(money)
        print('您已成功充值%s元' % money)
        break
    else:
        print('您输入了非法字符，请重新输入：')
flag = True
while flag:
    print('有如下商品供您选择：')
    for index, commodity_dict in enumerate(goods):
        print('{}\t{}\t{}'.format(index + 1, commodity_dict['name'], commodity_dict['price']))
    print('输入Q或q进行结算\n输入Q或q退出程序(如不结算购物车可直接退出)')
    select_num = input('请输入您的选择：').strip()
    if select_num.isdigit():
        select_num = int(select_num)
        if 0 < select_num <= len(goods):
            if (select_num - 1) not in goods_car:
                goods_car[select_num - 1] = { \
                    'name': goods[select_num - 1]['name'], 'price': goods[select_num - 1]['price'], 'amount': 1}
            else:
                goods_car[select_num - 1]['amount'] += 1
            print('您选择的商品具体信息：商品名称：{}商品价格：{}商品数量：1，并成功添加到购物车中。' \
                  .format(goods[select_num - 1]['name'], goods[select_num - 1]['price']))
        else:
            print('您输入的序号超出范围，请重新输入：')
    elif select_num.upper() == 'N':
        while 1:
            print('您购物车的具体商品如下：')
            total_price = 0
            for ind, com_dict in goods_car.items():
                print('序号：{}商品名称{}商品单价{}此商品总价：{}' \
                      .format(ind + 1, com_dict['name'], com_dict['price'], com_dict['price'] * com_dict['amount']))
                total_price += com_dict['price'] * com_dict['amount']
            print('————————> 总价格：%s元' % total_price)

            if money >= total_price:
                money = int(money)
                print('您已成功购买以上所有商品，余额为%s元，期待您的下次光临哟~' % money)
                flag = False
                break
            else:
                print('余额不足，还差%s元，请忍痛割爱，删掉一些商品' % (total_price - money))
                del_num = input('请输入要删除的商品序号：').strip()
                if del_num.isdigit():
                    del_num = int(del_num)
                    if (del_num - 1) in goods_car:
                        goods_car[del_num - 1]['amount'] -= 1
                        if not goods_car[del_num - 1]['amount']:
                            del goods_car[del_num - 1]
                    else:
                        print('您输入的序号超出范围，请重新输入：')
                else:
                    print('您输入了非数字元素，请重新输入：')
    elif select_num.upper() == 'Q':
        print('欢迎下次光临哟')
    else:
        print('您输入的选项不存在。请重新输入:')