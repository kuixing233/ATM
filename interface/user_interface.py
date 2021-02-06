"""
逻辑接口层
    用户接口
"""


from db import db_handle


# 注册接口
def register_interface(username, password, balance=15000):
    # 调用数据层
    user_dic = db_handle.select(username)

    # 用户已存在
    if user_dic:
        return False, '用户已存在'

    # 用户不存在
    user_dic = {
        'username': username,
        'password': password,
        'balance': balance,
        # 记录用户流水的列表
        'flow': [],
        # 记录用户的购物车
        'shop_car': {},
        # 记录用户是否被冻结
        'locked': False
    }

    db_handle.save(user_dic)

    return True, f'{username} 注册成功'