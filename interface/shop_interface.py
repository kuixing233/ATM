"""
购物商城接口
"""
from db import db_handle


# 商品准备结算接口
def shopping_interface(login_user, shopping_car):
    cost = 0
    for price_number in shopping_car.values():
        price, number = price_number

        cost += price * number

    from interface import bank_interface
    flag = bank_interface.pay_interface(
        login_user, cost
    )

    if flag:
        return True, '支付成功'
    return False, '支付失败，金额不足'


# 购物车添加接口
def add_shop_car_interface(login_user, shopping_car):
    user_dic = db_handle.select(login_user)

    shop_car = user_dic.get('shop_car')

    for shop_name, price_number in shopping_car.items():

        number = price_number[1]

        if shop_name in shop_car:
            user_dic['shop_car'][shop_name][1] += number

        else:
            user_dic['shop_car'].update(
                {shop_name: price_number}
            )

    db_handle.save(user_dic)
    return True, '添加购物车成功'
