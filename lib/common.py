"""
存放公共方法
"""


import hashlib


# md5加密
def get_pwd_md5(password):

    md5_obj = hashlib.md5()
    md5_obj.update(password.encode('utf-8'))
    salt = '你本无意穿堂风，偏偏孤倨引山洪'
    md5_obj.update(salt.encode('utf-8'))

    return md5_obj.hexdigest()