"""
银行相关业务接口
"""
from db import db_handle


# 提现接口（手续费5%）
def withdraw_interface(username, money):

    user_dic = db_handle.select(username)

    balance = int(user_dic['balance'])

    real_money = money * 1.05

    if balance >= real_money:
        user_dic['balance'] = balance - real_money
        db_handle.save(user_dic)
        return True, f'用户{username} 提现金额{money}成功, 手续费为：{money * 0.05}￥'

    return False, '余额不足，请重新输入'
