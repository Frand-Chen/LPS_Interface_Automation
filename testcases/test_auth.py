# -*- coding=utf-8 -*-

"""
auth 测试用例模块
"""

import pytest
import allure
from testcases import *
from openpyxl.styles import colors
from common.handle_data import get_test_data
from common.handle_request import handle_session_request as http
from common.logger import my_logger
from common.read_excel import ReadExcel


@allure.feature("获取 Auth 接口")
class TestAuth:
    """执行 Auth 测试用例"""
    # 获取 Auth 的测试用例数据
    excel = ReadExcel(test_case_path, "Auth")
    auth_test_data = excel.read_data_object()
    # 写测试结果的列数
    result_column = 11

    # 划分测试用例数据
    get_auth_normal_data = []
    get_auth_abnormal_data = []

    for data in auth_test_data:
        if data.flow == "normal":
            get_auth_normal_data.append(data)
        elif data.flow == "abnormal":
            get_auth_abnormal_data.append(data)
        elif data.flow == "skip":
            excel.write_data(row=data.case_id + 1, column=result_column, value="Skip", font_color=colors.PURPLE)

    @allure.story("正常获取 Auth")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("{test_data.title}")
    @pytest.mark.skip
    @pytest.mark.parametrize("test_data", get_auth_normal_data)
    def test_get_auth_normal(self, test_data):
        """测试 Auth 请求正常的用例"""
        case_id, interface, flow, title, method, url, params, headers, data, expected, check_sql = get_test_data(
            test_data)

        # 发送请求
        response = http.send(url=url, method=method, params=params, headers=headers)

        # 断言
        try:
            assert expected["code"] == response.status_code
            assert expected["field_1"] in response.json()
            assert expected["field_2"] in response.json()
        except AssertionError as e:
            self.excel.write_data(row=case_id + 1, column=self.result_column, value="Fail", font_color=colors.RED)
            my_logger.info("{} - {}：{} ---> Fail".format(interface, case_id, title))
            raise e
        else:
            self.excel.write_data(row=case_id + 1, column=self.result_column, value="Pass",
                                  font_color=colors.DARKGREEN)
            my_logger.info("{} - {}：{} ---> Pass".format(interface, case_id, title))

    @allure.story("异常获取 Auth")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("{test_data.title}")
    @pytest.mark.skip
    @pytest.mark.parametrize("test_data", get_auth_abnormal_data)
    def test_get_auth_abnormal(self, test_data):
        """测试 Auth 请求异常的用例"""
        case_id, interface, flow, title, method, url, params, headers, data, expected, check_sql = get_test_data(
            test_data)

        # 发送请求
        response = http.send(url=url, method=method, params=params, headers=headers)

        # 断言
        try:
            assert expected["code"] == response.status_code
        except AssertionError as e:
            self.excel.write_data(row=case_id + 1, column=self.result_column, value="Fail", font_color=colors.RED)
            my_logger.info("{} - {}：{} ---> Fail".format(interface, case_id, title))
            raise e
        else:
            self.excel.write_data(row=case_id + 1, column=self.result_column, value="Pass",
                                  font_color=colors.DARKGREEN)
            my_logger.info("{} - {}：{} ---> Pass".format(interface, case_id, title))


if __name__ == '__main__':
    pytest.main(["-s"])
