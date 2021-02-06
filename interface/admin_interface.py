from db import db_handle


def change_balance_interface(username, money):
    user_dic = db_handle.select(username)

    if user_dic:
        user_dic['balance'] = int(money)

        db_handle.save(user_dic)

        return True, '额度修改成功'

    return False, '修改额度用户不存在'


def lock_user_interface(username):
    user_dic = db_handle.select(username)

    if user_dic:
        user_dic['locked'] = True
        db_handle.save(user_dic)
        return True, f'用户[{username}]冻结成功'

    return False, '要冻结的用户不存在，请重新输入'
