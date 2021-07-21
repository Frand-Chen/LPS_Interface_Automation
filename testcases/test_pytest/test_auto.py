# -*- coding=utf-8 -*-
# import json
# import pytest
# from jsonpath import jsonpath
# from openpyxl.styles import colors
# from common.read_excel import ReadExcel
# from testcases import *
#
# title = """{
#     "matchCount": 0,
#     "nextResultSetExists": false,
#     "previousResultSetExists": false,
#     "pageIndex": 0,
#     "pageSize": 1,
#     "members": []
# }"""
#
# title_json = json.loads(title)
# print(jsonpath(title_json, "$.matchCount")[0])
# print(jsonpath(title_json, "$.members"))[0]
# print(type(title_json))
#
# title_str = json.dumps(title_json)
#
# print(type(title_str))
# import time

import pytest
import allure


@allure.feature("获取 auto 接口")
class TestAuto:

    @pytest.mark.xfail
    @allure.story("正常获取 auto")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_normal(self):
        # pytest.xfail("功能未完善")
        print("ddddddd")
        assert 1==2


if __name__ == '__main__':
    pytest.main(["-s"])



