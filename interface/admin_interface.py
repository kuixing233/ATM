from db import db_handle
from lib import common


admin_logger = common.get_logger('admin')


# 修改额度接口
def change_balance_interface(username, money):
    user_dic = db_handle.select(username)

    if user_dic:
        user_dic['balance'] = int(money)

        db_handle.save(user_dic)

        msg = f'管理员修改用户[{username}] 额度为：{money}, 修改成功'
        admin_logger.info(msg)
        return True, msg

    return False, '修改额度用户不存在'


# 冻结用户接口
def lock_user_interface(username):
    user_dic = db_handle.select(username)

    if user_dic:
        user_dic['locked'] = True
        db_handle.save(user_dic)
        return True, f'用户[{username}]冻结成功'

    return False, '要冻结的用户不存在，请重新输入'
