# -*- coding=utf-8 -*-

"""
该模块用来处理配置文件
"""
import os
from configparser import ConfigParser
from common.contents import CONF_DIR


class HandleConf(ConfigParser):
    """继承父类的方法"""

    def __init__(self, file_name, encoding="utf8"):
        # 调用类的方法及属性
        super().__init__()
        self.file_name = file_name
        self.encoding = encoding
        self.read(file_name, encoding)

    def write_data(self, section, option, value):
        """
        写入数据
        :param section: 配置块
        :param option: 配置项
        :param value: 配置值
        """
        # 如果配置文件中没有 section 则新建一个
        if not self.has_section(section):
            self.add_section(section)

        # 写入内容
        self.set(section=section, option=option, value=value)
        # 保存到文件
        self.write(open(self.file_name, "w", encoding=self.encoding))

    def rem_section(self, section):
        """删除 section"""
        self.remove_section(section)
        self.write(open(self.file_name, "w", encoding=self.encoding))

    def rem_option(self, option):
        """删除 option"""
        self.remove_section(option)
        self.write(open(self.file_name, "w", encoding=self.encoding))


# 获取配置文件的绝对路径
secrecy_conf_path = os.path.join(CONF_DIR, "secrecy_config.ini")
general_conf_path = os.path.join(CONF_DIR, "general_config.ini")

# 私密配置对象
sec_conf = HandleConf(secrecy_conf_path)
# 一般配置对象
gen_conf = HandleConf(general_conf_path)

if __name__ == '__main__':
    # gen_conf["DEFAULT"] = {'ServerAliveInterval': '455',
    #                        'Compression': 'yes',
    #                        'CompressionLevel': '9',
    #                        'ForwardX11': 'yes'
    #                        }
    # gen_conf.write(open(general_conf_path, "w", encoding="utf8"))
    print(gen_conf.get("logging", "level"))
