"""
逻辑接口层
    用户接口
"""

from db import db_handle
from lib import common

user_logger = common.get_logger('user')


# 注册接口
def register_interface(username, password, balance=15000):
    # 调用数据层
    user_dic = db_handle.select(username)

    # 用户已存在
    if user_dic:
        return False, '用户已存在'

    # 用户不存在
    password = common.get_pwd_md5(password)

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

    msg = f'用户[{username}] 注册成功'
    user_logger.info(msg)
    return True, msg


# 登录接口
def login_interface(username, password):
    user_dic = db_handle.select(username)

    if user_dic:
        if user_dic['locked']:
            return False, '当前用户已被锁定'

        password = common.get_pwd_md5(password)
        if password == user_dic.get('password'):
            msg = f'用户 [{username}] 登录成功！'
            user_logger.info(msg)
            return True, msg

        msg = f'用户 [{username}] 密码错误,登录失败！'
        user_logger.warn(msg)
        return False, '密码错误'

    return False, f'用户 [{username}] 不存在,登录失败！'


# 查看余额接口
def check_bal_interface(username):
    user_dic = db_handle.select(username)
    return user_dic['balance']


# 查看购物车接口
def check_shop_car_interface(username):
    user_dic = db_handle.select(username)

    return user_dic['shop_car']