# -*- coding=utf-8 -*-

"""
members 测试用例模块
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


@allure.feature("获取 Member 信息接口")
class TestMembers:
    """执行 Members 测试用例"""
    # 获取 Members 的测试用例数据
    excel = ReadExcel(test_case_path, "Members")
    members_test_data = excel.read_data_object()
    # 写测试结果的列数
    result_column = 11

    # 划分测试用例数据
    members_normal_data = []
    members_abnormal_data = []
    for data in members_test_data:
        if data.flow == "normal":
            members_normal_data.append(data)
        elif data.flow == "abnormal":
            members_abnormal_data.append(data)
        elif data.flow == "skip":
            excel.write_data(row=data.case_id + 1, column=result_column, value="Skip", font_color=colors.PURPLE)

    @allure.story('正常获取会员信息')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("{test_data.title}")
    @pytest.mark.skip
    @pytest.mark.parametrize("test_data", members_normal_data)
    def test_members_normal(self, test_data, get_session):
        """测试 members 请求正常的用例"""
        case_id, interface, flow, title, method, url, params, headers, data, expected, check_sql = get_test_data(
            test_data)

        # 发送请求
        response = http.send(url=url, method=method, params=params, headers=headers)

        # 断言
        try:
            assert expected["code"] == response.status_code
            assert expected["number"] == jsonpath(response.json(), "$.members[0].number")[0]
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
    @allure.title("{test_data.title}")
    @pytest.mark.skip
    @pytest.mark.parametrize("test_data", members_abnormal_data)
    def test_members_abnormal(self, test_data, get_session):
        """测试 members 请求异常的用例"""
        case_id, interface, flow, title, method, url, params, headers, data, expected, check_sql = get_test_data(
            test_data)

        # 发送请求
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

        except AssertionError as e:
            self.excel.write_data(row=case_id + 1, column=self.result_column, value="Fail", font_color=colors.RED)
            raise e
        else:
            self.excel.write_data(row=case_id + 1, column=self.result_column, value="Pass",
                                  font_color=colors.DARKGREEN)

    # @classmethod
    # def setup_class(cls):
    #     my_logger.info("setup_class")
    #
    # @classmethod
    # def teardown_class(cls):
    #     my_logger.info("teardown_class")
    #
    # def setup(self):
    #     my_logger.info("setup")
    #
    # def teardown(self):
    #     my_logger.info("teardown")
    #
    # test_data_demo = [1]
    #
    # @pytest.mark.parametrize("data1", test_data_demo)
    # @pytest.mark.usefixtures("get_demo")
    # def test_demo(self, data1):
    #     my_logger.info("test_demo{}".format(data1))
    #
    # @pytest.mark.run(order=0)
    # @pytest.mark.skip
    # @pytest.mark.parametrize(("data1", "data2"), [(1, 2), (4, 5)])
    # def test_demo2(self, data1, data2):
    #     print("0", data1, data2)
    #
    # @pytest.mark.run(order=1)
    # @pytest.mark.skip
    # @pytest.mark.parametrize(("data1", "data2"), [(3, 5), (7, 8)])
    # @allure.feature('购物车功能')
    # @allure.story('加入购物车')
    # @allure.step('demo测试')
    # def test_demo1(self, data1, data2):
    #     with allure.step("浏览商品"):  # 步骤2，step的参数将会打印到测试报告中
    #         allure.attach('笔记本', '商品1')  # attach可以打印一些附加信息
    #         allure.attach('手机', '商品2')
    #
    #     with allure.step("校验结果"):  # 步骤4
    #         allure.attach('添加购物车成功', '期望结果', data1)
    #         allure.attach('添加购物车失败', '实际结果', data2)
    #         assert 1 > 2


if __name__ == '__main__':
    pytest.main(["-s"])
