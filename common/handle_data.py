# -*- coding=utf-8 -*-

"""
该模块用来处理测试用例的数据
"""

import re
from common.handle_config import gen_conf, sec_conf


class TestData:
    """保存需要替换的数据"""
    pass


def replace_data(section, data) -> str:
    """
    替换数据
    :param config_file: 配置文件
    :param section: 配置块
    :param data: 需要替换的数据
    :return: data
    """
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
            try:
                # 根据替换内容 item"#***#" 到 secrecy_config 配置文件中查找对应的数据 key "***"，并进行替换
                data = data.replace(item, str(sec_conf.get(section, key)))
            except:
                # 根据替换内容 item"#***#" 到 general_config 配置文件中查找对应的数据 key "***"，并进行替换
                data = data.replace(item, str(gen_conf.get(section, key)))
        except:
            # 如果配置文件中没有对应的 key,则到 TestDate 中查找
            data = data.replace(item, str(getattr(TestData, key)))


    return data


def get_test_data(test_data):
    """获取测试用例的数据"""
    case_id = test_data.case_id
    interface = test_data.interface
    flow = test_data.flow
    title = test_data.title
    method = test_data.method
    base_url = sec_conf.get("environment", "base_url")
    url = base_url + replace_data("environment", test_data.url)
    params = test_data.params
    if params != None:
        params = eval(replace_data("testdata", params))
    data = test_data.data
    if data != None:
        data = eval(data)
    expected = test_data.expected
    if expected != None:
        expected = eval(expected)
    headers = eval(sec_conf.get("environment", "headers"))
    check_sql = test_data.check_sql
    return case_id, interface, flow, title, method, url, params, headers, data, expected, check_sql


if __name__ == '__main__':
    # data = replace_data("#phone#,#name#")
    dic = 'vNext2/api/#version#/session?propertyCode=#propertyCode#'
    data = replace_data(dic)
    print(type(data))
    print(data)
