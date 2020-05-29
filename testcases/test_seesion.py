# -*- coding=utf-8 -*-

"""
session 测试用例模块
"""

import pytest
import os

from common.contents import DATA_DIR
from common.handle_config import gen_conf, sec_conf
from common.handle_data import replace_data
from common.handle_request import handle_session_request as http
from common.logger import my_logger
from common.read_excel import ReadExcel

# 获取 Session 测试用例数据
test_case_file = gen_conf.get("testdata", "test_case_file")
test_case_path = os.path.join(DATA_DIR, test_case_file)
excel = ReadExcel(test_case_path, "Session")
session_test_data = excel.read_data_object()


class TestSession:

    @pytest.mark.parametrize("test_info", session_test_data[0:1])
    def test_session(self, test_info):
        # 测试数据
        case_id = test_info.case_id
        title = test_info.title
        method = test_info.method
        base_url = sec_conf.get("environment", "base_url")
        url = base_url + replace_data(test_info.url)
        host = sec_conf.get("environment", "host")
        akey = sec_conf.get("environment", "AKey")
        headers = eval(sec_conf.get("environment", "headers"))
        headers["AKey"] = akey
        headers["Host"] = host
        response = http.send(url=url, method=method, headers=headers)
        print(response.json())


if __name__ == '__main__':
    pytest.main(["-s"])
