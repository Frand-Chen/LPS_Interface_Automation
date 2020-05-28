# -*- coding=utf-8 -*-

"""
该模块用来处理测试用例的数据
"""

import re
from common.handle_config import gen_conf


class TestData:
    """保存需要替换的数据"""
    pass


def replace_data(data):
    # 匹配规则
    r = r"#(.+?)#"
    # 根据规则，判断是否需要替换数据
    while re.search(r, data):
        # 匹配第一个要替换的数据
        res = re.search(r, data)
        # 提取待替换的数据 #***#
        item = res.group()
        # 获取替换内容中的数据项
        key = res.group(1)

        try:
            # 根据替换内容 item"#***#" 到配置文件中查找对应的数据 key "***"，并进行替换
            data = data.replace(item, str(gen_conf.get("test_data", key)))
        except:
            # 如果配置文件中没有对应的 key,则到 TestDate 中查找,
            data = data.replace(item, str(getattr(TestData(), key)))

    return data


if __name__ == '__main__':
    # data = replace_data("#phone#,#name#")
    dic = '{"member_id":#admin_member_id#+1}'
    data = replace_data(dic)
    print(type(data))
    print(eval(data))
    print(type(data))
    print(eval(data))

