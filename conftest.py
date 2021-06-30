# -*- coding=utf-8 -*-

"""
该模块用来处理 allure 测试环境信息
"""
from common.handle_config import sec_conf

membership_system = sec_conf.get("environment", "membership_system")
version = sec_conf.get("environment", "version")
host = sec_conf.get("environment", "host")


def pytest_sessionfinish(session):
    """写入测试环境信息到 allure 报告中"""
    # environment.properties 文件位置、名称固定
    with open("{}/report_data/environment.properties".format(session.config.rootdir), "w") as f:
        f.write("membership_system={}\n"
                "version={}\n"
                "host={}".format(membership_system, version, host))
