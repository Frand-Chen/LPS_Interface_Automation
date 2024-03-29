# -*- coding=utf-8 -*-

"""
Members 测试用例模块
"""

import pytest
from testcases import *
from openpyxl.styles import colors
import allure
from jsonpath import jsonpath
from common.handle_data import get_test_data
from common.handle_request import handle_session_request as http
from common.logger import my_logger
from common.read_excel import ReadExcel


@allure.feature("查询 Member 信息接口")
class TestMembers:
    """执行 Members 测试用例"""
    # 获取 Members 的测试用例数据
    excel = ReadExcel(test_case_path, "Members")
    member_test_data = excel.read_data_object()
    # 写测试结果的列数
    result_column = 11

    # 划分测试用例数据
    get_member_normal_data = []
    get_member_abnormal_data = []
    for data in member_test_data:
        if data.flow == "normal":
            get_member_normal_data.append(data)
        elif data.flow == "abnormal":
            get_member_abnormal_data.append(data)
        elif data.flow == "skip":
            excel.write_data(row=data.case_id + 1, column=result_column, value="Skip", font_color=colors.PURPLE)

    @allure.story('正常获取会员信息')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("{test_data.case_id}.{test_data.title}")
    # @pytest.mark.skip
    @pytest.mark.parametrize("test_data", get_member_normal_data)
    def test_member_normal(self, test_data, get_session):
        """测试 members 请求正常的用例"""
        case_id, interface, flow, title, method, url, params, headers, data, expected, check_sql = get_test_data(
            test_data)

        # 发送请求
        response = http.send(url=url, method=method, params=params, headers=headers)

        # 断言
        try:
            assert expected["code"] == response.status_code
            if title in ["通过会员名查询", "通过会员姓查询", "通过相关联的会员姓和名组合查询"]:
                assert expected["id"] in jsonpath(response.json(), "$.members[0:].id")
                assert jsonpath(response.json(), "$.matchCount")[0] >= 1
                assert expected["firstName"] in jsonpath(response.json(), "$.members[0:].firstName")
                assert expected["lastName"] in jsonpath(response.json(), "$.members[0:].lastName")
            else:
                assert expected["id"] == jsonpath(response.json(), "$.members[0].id")[0]
                assert expected["matchCount"] == jsonpath(response.json(), "$.matchCount")[0]
                assert expected["firstName"] == jsonpath(response.json(), "$.members[0].firstName")[0]
                assert expected["lastName"] == jsonpath(response.json(), "$.members[0].lastName")[0]
        except AssertionError as e:
            self.excel.write_data(row=case_id + 1, column=self.result_column, value="Fail",
                                  font_color=colors.RED)
            my_logger.info("{} - {}：{} ---> Fail".format(interface, case_id, title))
            raise e
        else:
            self.excel.write_data(row=case_id + 1, column=self.result_column, value="Pass",
                                  font_color=colors.DARKGREEN)
            my_logger.info("{} - {}：{} ---> Pass".format(interface, case_id, title))

    @allure.story('异常获取会员信息')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("{test_data.case_id}.{test_data.title}")
    # @pytest.mark.skip
    @pytest.mark.parametrize("test_data", get_member_abnormal_data)
    def test_member_abnormal(self, test_data, get_session):
        """测试 members 请求异常的用例"""
        case_id, interface, flow, title, method, url, params, headers, data, expected, check_sql = get_test_data(
            test_data)

        # 发送请求
        response = http.send(url=url, method=method, params=params, headers=headers)

        # 断言
        try:
            if title in ["错误的companyName"]:
                assert expected["code"] == response.status_code
                assert expected["id"] == jsonpath(response.json(), "$.members[0].id")[0]
                assert expected["firstName"] == jsonpath(response.json(), "$.members[0].firstName")[0]
                assert expected["lastName"] == jsonpath(response.json(), "$.members[0].lastName")[0]
            elif title in ["查询不存在的会员卡号", "查询错误的邮箱地址", "查询不存在的会员名",
                           "查询不存在的会员姓", "通过不相关的会员姓和名组合查询",
                           "查询不存在的手机号,11位数", "查询错误的手机号,超过11位数",
                           "查询错误的手机号,小于11位数"]:
                assert expected["code"] == response.status_code
                assert expected["matchCount"] == jsonpath(response.json(), "$.matchCount")[0]
                assert expected["members"] == jsonpath(response.json(), "$.members")[0]
            else:
                assert expected["code"] == response.status_code

        except AssertionError as e:
            self.excel.write_data(row=case_id + 1, column=self.result_column, value="Fail", font_color=colors.RED)
            my_logger.info("{} - {}：{} ---> Pass".format(interface, case_id, title))
            raise e
        else:
            self.excel.write_data(row=case_id + 1, column=self.result_column, value="Pass",
                                  font_color=colors.DARKGREEN)
            my_logger.info("{} - {}：{} ---> Pass".format(interface, case_id, title))


if __name__ == '__main__':
    pytest.main(["-s"])
