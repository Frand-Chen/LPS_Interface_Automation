# -*- coding=utf-8 -*-

"""
该模块用来处理前置/后置条件
"""

import pytest
from jsonpath import jsonpath

from common.handle_config import sec_conf
from common.handle_data import TestData
from common.handle_request import handle_session_request as http
from common.logger import my_logger


@pytest.fixture()
def get_headers_info():
    """获取 headers 信息"""
    base_url = sec_conf.get("environment", "base_url")
    version = sec_conf.get("environment", "version")
    headers = eval(sec_conf.get("environment", "headers"))
    headers["AKey"] = sec_conf.get("environment", "AKey")
    headers["Host"] = sec_conf.get("environment", "host")

    return base_url, version, headers


@pytest.fixture()
def get_session(get_headers_info):
    """获取 session, 并保存"""
    base_url, version, headers = get_headers_info
    url = base_url + "vNext2/api/{}/session".format(version)
    response = http.send(url=url, method="get", headers=headers)
    session_id = jsonpath(response.json(), "$..sessionId")[0]
    session_expiry = jsonpath(response.json(), "$..sessionExpiry")[0]
    # 保存数据到 TestData 类中
    setattr(TestData, "seesionId", session_id)
    setattr(TestData, "sessionExpiry", session_expiry)


def get_auth(get_headers_info):
    """获取 auth, 并保存"""
    base_url, version, headers = get_headers_info
    url = base_url + "vNext2/api/{}/login".format(version)
    response = http.send(url=url, method="get", headers=headers)
    token = jsonpath(response.json(), "$..accessToken")[0]
    token_expiry = jsonpath(response.json(), "$..accessTokenExpiry")[0]
    # 保存数据到 TestData 类中
    setattr(TestData, "accessToken", token)
    setattr(TestData, "accessTokenExpiry", token_expiry)
