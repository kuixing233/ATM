"""
存放公共方法
"""


import hashlib
import logging.config
from conf import settings


# md5加密
def get_pwd_md5(password):

    md5_obj = hashlib.md5()
    md5_obj.update(password.encode('utf-8'))
    salt = '你本无意穿堂风，偏偏孤倨引山洪'
    md5_obj.update(salt.encode('utf-8'))

    return md5_obj.hexdigest()


# 登录认证装饰器
def login_auth(func):
    from core import src


    def inner(*args, **kwargs):
        if src.login_user:
            res = func(*args, **kwargs)
            return res
        else:
            print('未出示证明，无法享受美好的功能服务!')
            src.login()

    return inner


# 添加日志功能
def get_logger(log_type):
    # 1、加载日志配置信息
    logging.config.dictConfig(
        settings.LOGGING_DIC
    )

    # 2、获取日志对象
    logger = logging.getLogger(log_type)

    return logger
