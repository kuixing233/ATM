"""
用户视图层
"""


from interface import user_interface, bank_interface
from lib import common


# 定义一个全局变量，保存用户登录状态
login_user = None


# 1、注册功能
def register():
    while True:
        # 1）让用户输入用户名与密码进行校验
        username = input("请输入用户名：").strip()
        password = input("请输入密码：").strip()
        re_password = input("请确认密码：").strip()

        if password == re_password:
            flag, msg = user_interface.register_interface(
                username, password
            )

            # 注册成功，结束
            if flag:
                print(msg)
                break

            # 注册失败，重新进入
            else:
                print(msg)


# 2、登录功能
def login():
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()

        flag, msg = user_interface.login_interface(
            username, password
        )

        if flag:
            print(msg)
            global login_user
            login_user = username
            break

        else:
            print(msg)


# 3、查看余额
@common.login_auth
def check_balance():

    balance = user_interface.check_bal_interface(
        login_user
    )

    print(f'用户{login_user} 账户余额为：{balance}')


# 4、提现功能
@common.login_auth
def withdraw():
    while True:
        input_money = input('请输入提现金额：').strip()

        if not input_money.isdigit():
            print('请重新输入')
            continue

        input_money = int(input_money)

        flag, msg = bank_interface.withdraw_interface(
            login_user, input_money
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)


# 5、还款功能
@common.login_auth
def repay():
    pass


# 6、转账功能
@common.login_auth
def tranfer():
    pass


# 7、查看流水
@common.login_auth
def check_flow():
    pass


# 8、购物功能
@common.login_auth
def shopping():
    pass


# 9、查看购物车
def check_shop_car():
    pass


# 10、管理员功能
def admin():
    pass


# 创建函数功能字典：
func_dic = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': tranfer,
    '7': check_flow,
    '8': shopping,
    '9': check_shop_car,
    '10': admin,
}


# 视图层主程序
def run():
    while True:
        print("""
        ====== ATM + 购物车 ======
            1、注册功能
            2、登录功能
            3、查看余额
            4、提现功能
            5、还款功能
            6、转账功能
            7、查看流水
            8、购物功能
            9、查看购物车
            10、管理员功能
        ======     end     ======
        """)

        choice = input("请输入功能编号：").strip()

        if choice not in func_dic:
            print("请输入正确的功能编号！")
            continue

        func_dic.get(choice)()
