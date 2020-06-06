# -*- coding=utf-8 -*-

"""
members 测试用例模块
"""
import pytest
from testcases import *
from openpyxl.styles import colors

from jsonpath import jsonpath
from common.handle_config import sec_conf
from common.handle_data import get_test_data, TestData
from common.handle_request import handle_session_request as http
from common.logger import my_logger
from common.read_excel import ReadExcel


class TestMembers:
    """执行 Members 测试用例"""
    # 获取 Members 的测试用例数据
    excel = ReadExcel(test_case_path, "Members")
    members_test_data = excel.read_data_object()
    # 写测试结果的列数
    result_column = 10

    @pytest.mark.skip
    @pytest.mark.parametrize("test_data", members_test_data)
    def test_members_normal(self, test_data, get_session):
        """测试 members 请求正常的用例"""
        if test_data.interface == "Members" and test_data.flow == "normal":
            # 测试数据
            case_id, interface, flow, title, method, url, params, headers, data, expected, check_sql = get_test_data(
                test_data)
            headers["Host"] = sec_conf.get("environment", "host")
            headers["AKey"] = sec_conf.get("environment", "Akey")
            headers["Session"] = getattr(TestData, "sessionId")
            response = http.send(url=url, method=method, params=params, headers=headers)
            response_json_data = response.json()
            # 断言
            try:
                assert expected["code"] == response.status_code
                assert expected["number"] == jsonpath(response_json_data, "$.members[0].number")[0]
                assert expected["firstName"] == jsonpath(response_json_data, "$.members[0].firstName")[0]
                assert expected["lastName"] == jsonpath(response_json_data, "$.members[0].lastName")[0]
            except AssertionError as e:
                self.excel.write_data(row=case_id + 1, column=self.result_column, value="Fail",
                                      font_color=colors.RED)
                my_logger.info("{} - {}：{} ---> Fail".format(interface, case_id, title))
                raise e
            else:
                self.excel.write_data(row=case_id + 1, column=self.result_column, value="Pass",
                                      font_color=colors.DARKGREEN)
                my_logger.info("{} - {}：{} ---> Pass".format(interface, case_id, title))

    # @pytest.mark.skip
    @pytest.mark.parametrize("test_data", members_test_data[1:3])
    def test_members_abnormal(self, test_data, get_session):
        """测试 members 请求异常的用例"""
        if test_data.interface == "Members" and test_data.flow == "abnormal":
            # 测试数据
            case_id, interface, flow, title, method, url, params, headers, data, expected, check_sql = get_test_data(
                test_data)
            headers["Host"] = sec_conf.get("environment", "host")
            headers["Akey"] = sec_conf.get("environment", "AKey")
            headers["Session"] = getattr(TestData, "sessionId")

            response = http.send(url=url, method=method, params=params, headers=headers)
            # 断言
            try:
                if title == "错误的companyName":
                    assert expected["code"] == response.status_code
                    assert expected["matchCount"] == jsonpath(response.json(), "$.matchCount")[0]
                    assert expected["members"] == jsonpath(response.json(), "$.members")
                elif title == "缺少companyName":
                    print(response.status_code)
                    assert expected["code"] == response.status_code
                    ass


            except AssertionError as e:
                self.excel.write_data(row=case_id + 1, column=self.result_column, value="Fail", font_color=colors.RED)
                raise e
            else:
                self.excel.write_data(row=case_id + 1, column=self.result_column, value="Pass",
                                      font_color=colors.DARKGREEN)


if __name__ == '__main__':
    pytest.main(["-s"])
