"""
数据处理层
 - 专门用于处理数据
"""


import json
import os
from conf import settings


# 查看数据
def select(user_name):
    user_path = os.path.join(
        settings.USER_DATA_PATH, f'{user_name}.json'
    )

    if os.path.exists(user_path):
        with open(user_path, 'r', encoding='utf-8') as f:
            user_dic = json.load(f)
            return user_dic


# 保存数据
def save(user_dic):
    username = user_dic.get('username')
    user_path = os.path.join(
        settings.USER_DATA_PATH, f'{username}.json'
    )

    with open(user_path, 'w', encoding='utf-8') as f:
        json.dump(user_dic, f, ensure_ascii=False)
