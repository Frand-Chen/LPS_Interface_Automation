# -*- coding=utf-8 -*-

"""
该模块用来处理配置文件
"""
from configparser import ConfigParser
from common.contents import CONF_DIR
import os


class HandleConf(ConfigParser):
    """继承父类的方法"""

    def __init__(self, file_name, encoding="utf8"):
        # 调用类的方法及属性
        super().__init__()
        self.file_name = file_name
        self.encoding = encoding
        self.read(file_name, encoding)

    def write_data(self):
        pass


# 获取配置文件的绝对路径
conf_path = os.path.join(CONF_DIR, "config.ini")
conf = HandleConf(conf_path)
