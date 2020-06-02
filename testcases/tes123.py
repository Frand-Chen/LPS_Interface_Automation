# -*- coding=utf-8 -*-
import re

from common.handle_config import sec_conf, gen_conf


class TestData:
    """保存需要替换的数据"""
    # propertyCode = "k0088123"
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
            # 根据替换内容 item"#***#" 到 secrecy_config 配置文件中查找对应的数据 key "***"，并进行替换
            try:
                print(1)
                data = data.replace(item, str(sec_conf.get(section, key)))
            except:
                print(2)
                # 根据替换内容 item"#***#" 到 general_config 配置文件中查找对应的数据 key "***"，并进行替换
                data = data.replace(item, str(gen_conf.get(section, key)))
        except:
            print(3)
            # 如果配置文件中没有对应的 key,则到 TestDate 中查找
            data = data.replace(item, str(getattr(TestData, key)))
        # try:
        #     data = data.replace(item, str(sec_conf.get("testdata", key)))
        # except:
        #     data = data.replace(item, str(gen_conf.get("testdata", key)))

    return data


data = replace_data("testdata", '{"propertyCode":"#propertyCode#"}')
print(data)

