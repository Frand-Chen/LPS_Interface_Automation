# -*- coding=utf-8 -*-

"""
该模块用来处理整个项目目录的路径
"""

import os

# # 获取当前文件夹的绝对路径
# dirname = os.path.dirname(__file__)
# # 获取当前文件的绝对路径
# abspath = os.path.abspath(__file__)
# print(dirname)
# print(abspath)

# 项目目录的路径 | 如果运行时项目目录路径出错，使用 abspath 方式获取当前文件的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# 配置文件的路径
CONF_DIR = os.path.join(BASE_DIR, "config")
# 测试用例数据的路径
DATA_DIR = os.path.join(BASE_DIR, "data")
# 日志文件的路径
LOG_DIR = os.path.join(BASE_DIR, "logs")
# 测试报告的路径
REPORT_DIR = os.path.join(BASE_DIR, "reports")
# 测试用例的路径
CASE_DIR = os.path.join(BASE_DIR, "testcases")