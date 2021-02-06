from core import src
from interface import admin_interface


def add_user():
    src.register()


def change_balance():
    while True:
        username = input('请输入用户账号：').strip()
        money = input('请输入要修改为的额度：').strip()

        if not money.isdigit():
            print('输入额度有误，请重新输入')
            continue

        flag, msg = admin_interface.change_balance_interface(
            username, money
        )

        if flag:
            print(msg)
            break;
        else:
            print(msg)


def lock_user():
    while True:
        username = input('请输入用户账号：').strip()

        flag, msg = admin_interface.lock_user_interface(
            username
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)


admin_func = {
    '1': add_user,
    '2': change_balance,
    '3': lock_user,
}


def admin_run():
    while True:
        print("""
        1、添加账户
        2、用户额度
        3、冻结账户
        """)
        choice = input("请输入管理员功能编号：").strip()

        if choice not in admin_func:
            print('请重新输入')
            continue

        admin_func.get(choice)()

