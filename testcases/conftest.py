# -*- coding=utf-8 -*-

"""
该模块用来处理前置/后置条件
"""

import pytest
from jsonpath import jsonpath

from common.handle_config import sec_conf
from common.handle_data import TestData
from common.handle_request import handle_session_request as http


@pytest.fixture()
def get_session():
    """获取 session"""
    version = sec_conf.get("environment", "version")
    url = sec_conf.get("environment", "base_url") + "vNext2/api/{}/session".format(version)
    headers = eval(sec_conf.get("environment", "headers"))
    headers["AKey"] = sec_conf.get("environment", "AKey")
    headers["Host"] = sec_conf.get("environment", "host")
    response = http.send(url=url, method="get", headers=headers)
    session_id = jsonpath(response.json(), "$..sessionId")[0]
    session_expiry = jsonpath(response.json(), "$..sessionExpiry")[0]
    # 保存数据到 TestData 类中
    setattr(TestData, "sessionId", session_id)
    setattr(TestData, "sessionExpiry", session_expiry)
