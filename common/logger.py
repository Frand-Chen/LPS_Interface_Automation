# -*- coding=utf-8 -*-

"""
该模块用来处理日志
"""

import logging
import os

from common.contents import LOG_DIR
from common.handle_config import gen_conf

# 获取配置文件中的 log 等级
level = gen_conf.get("logging", "level")
file_level = gen_conf.get("logging", "file_level")
console_level = gen_conf.get("logging", "console_level")

# 获取日志文件的绝对路径
file_name = gen_conf.get("logging", "file_name")
log_file_path = os.path.join(LOG_DIR, file_name)


class Logger:
    # 静态方法，直接通过类名调用
    @staticmethod
    def create_logger():
        # 创建一个名为 my_log 的日志收集器
        my_log = logging.getLogger("my_log")
        # 设置日志收集器的等级
        my_log.setLevel(level=level)

        # 1.添加输出渠道(输出到 python 控制台)
        console_log = logging.StreamHandler()
        # 设置输出等级
        console_log.setLevel(console_level)
        # 把输出渠道绑到日志收集器上
        my_log.addHandler(console_log)

        # 2.添加输出渠道(输出到日志文件)
        file_log = logging.FileHandler(log_file_path, encoding="utf8")
        # 设置输出等级
        file_log.setLevel(file_level)
        my_log.addHandler(file_log)

        # 设置日志输出格式
        log_format = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')

        # 将日志输出格式和输出渠道绑定
        console_log.setFormatter(log_format)
        file_log.setFormatter(log_format)

        return my_log


# 创建一个日志收集器
my_logger = Logger.create_logger()

if __name__ == '__main__':
    my_logger.info("info123")
    my_logger.error("error456")
