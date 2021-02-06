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

        flow = f'用户：{username} 提现金额{money}成功, 手续费为：{money * 0.05}￥'
        user_dic['flow'].append(flow)

        db_handle.save(user_dic)

        return True, flow

    return False, '余额不足，请重新输入'


# 还款接口
def repay_interface(username, money):
    user_dic = db_handle.select(username)

    user_dic['balance'] += money

    flow = f"用户：[{username}] 还款{money}￥ 成功, 当前额度为：{user_dic['balance']}"
    user_dic['flow'].append(flow)

    db_handle.save(user_dic)

    return True, flow


# 转账接口
def transfer_interface(username, to_username, money):
    if not db_handle.select(to_username):
        return False, '接收人不存在，请重新输入'

    user_dic_now = db_handle.select(username)
    user_dic_to = db_handle.select(to_username)

    balance_now = int(user_dic_now['balance'])

    if balance_now >= money:
        user_dic_now['balance'] -= money
        user_dic_to['balance'] += money

        flow_now = f'用户：[{username}] 给 用户：[{to_username}] 转账：{money}￥ 成功'
        user_dic_now['flow'].append(flow_now)

        flow_to = f'用户：[{to_username}] 接收 用户：[{username}] 转账：{money}￥ 成功'
        user_dic_to['flow'].append(flow_to)

        db_handle.save(user_dic_now)
        db_handle.save(user_dic_to)

        return True, flow_now

    return False, '余额不足'


# 查看流水
def check_flow(username):
    return db_handle.select(username).get('flow')
