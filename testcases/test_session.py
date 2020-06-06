# -*- coding=utf-8 -*-

"""
session 测试用例模块
"""

import pytest
import os

from openpyxl.styles import colors
from common.contents import DATA_DIR
from common.handle_config import gen_conf, sec_conf
from common.handle_data import get_test_data, TestData
from common.handle_request import handle_session_request as http
from common.logger import my_logger
from common.read_excel import ReadExcel

# 获取测试用例文件
test_case_file = gen_conf.get("testdata", "test_case_file")
test_case_path = os.path.join(DATA_DIR, test_case_file)


class TestSession:
    """执行 Session 测试用例"""
    # 获取 Session 的测试用例数据
    excel = ReadExcel(test_case_path, "Session")
    session_test_data = excel.read_data_object()
    # 写测试结果的列数
    result_column = 10

    # @pytest.mark.skip
    @pytest.mark.normal
    @pytest.mark.parametrize("test_data", session_test_data)
    def test_get_session_normal(self, test_data):
        """测试 getSession 请求正常的用例"""
        if test_data.interface == "getSession" and test_data.flow == "normal":
            # 测试数据
            case_id, interface, flow, title, method, url, params, headers, data, expected, check_sql = get_test_data(
                test_data)
            headers["AKey"] = sec_conf.get("environment", "AKey")
            headers["Host"] = sec_conf.get("environment", "host")

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
                # Auth-用例title：成功获取Token ---> Pass
                raise e
            else:
                self.excel.write_data(row=case_id + 1, column=self.result_column, value="Pass",
                                      font_color=colors.DARKGREEN)
                my_logger.info("{} - {}：{} ---> Pass".format(interface, case_id, title))

    @pytest.mark.skip
    @pytest.mark.abnormal
    @pytest.mark.parametrize("test_data", session_test_data)
    def test_get_session_abnormal(self, test_data):
        """测试 getSession 请求异常的用例"""
        if test_data.interface == "getSession" and test_data.flow == "abnormal":
            case_id, interface, flow, title, method, url, params, headers, data, expected, check_sql = get_test_data(
                test_data)
            headers["Host"] = sec_conf.get("environment", "host")
            if title == "错误的AKey":
                headers["AKey"] = sec_conf.get("environment", "errorAKey")
            elif title == "缺少AKey":
                headers["AKey"] = None

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

    @pytest.mark.skip
    @pytest.mark.normal
    @pytest.mark.parametrize("test_data", session_test_data)
    def test_delete_session_normal(self, test_data, get_session):
        """测试 deleteSession 请求正常的用例"""
        if test_data.interface == "deleteSession" and test_data.flow == "normal":
            case_id, interface, flow, title, method, url, params, headers, data, expected, check_sql = get_test_data(
                test_data)
            headers["AKey"] = sec_conf.get("environment", "AKey")
            headers["Host"] = sec_conf.get("environment", "host")

            # 发送请求
            response = http.send(url=url, method=method, headers=headers)

            # 断言
            try:
                assert expected["code"] == response.status_code
            except AssertionError as e:
                self.excel.write_data(row=case_id, column=self.result_column, value="Fail", font_color=colors.RED)
                my_logger.info("{} - {}：{} ---> Fail".format(interface, case_id, title))
                raise e
            else:
                self.excel.write_data(row=case_id + 1, column=self.result_column, value="Pass",
                                      font_color=colors.DARKGREEN)
                my_logger.info("{} - {}：{} ---> Pass".format(interface, case_id, title))

    @pytest.mark.skip
    @pytest.mark.abnormal
    @pytest.mark.parametrize("test_data", session_test_data)
    def test_delete_session_abnormal(self, test_data, get_session):
        """测试 deleteSessoin 请求异常的用例"""
        if test_data.interface == "deleteSession" and test_data.flow == "abnormal":
            case_id, interface, flow, title, method, url, params, headers, data, expected, check_sql = get_test_data(
                test_data)
            headers["Host"] = sec_conf.get("environment", "host")

            if title == "缺少sessionId":
                headers["AKey"] = sec_conf.get("environment", "errorAKey")
            elif title == "错误的seesionId":
                headers["AKey"] = sec_conf.get("environment", "AKey")
            elif title == "错误的AKey":
                headers["AKey"] = "8D1097CD-40DF-4BA2-8EFD-CCD896798B23"
            elif title == "缺少AKey":
                headers["AKey"] = None

            response = http.send(url=url, method=method, headers=headers)

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
