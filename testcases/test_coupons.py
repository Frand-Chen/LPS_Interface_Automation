# -*- coding=utf-8 -*-

"""
coupons 测试用例模块
"""

import allure
import pytest
from openpyxl.styles import colors

from common.handle_data import get_test_data
from common.handle_request import handle_session_request as http
from common.logger import my_logger
from common.read_excel import ReadExcel
from testcases import *


@allure.feature("查询/兑换/退还 Coupon 接口")
class TestCoupons:
    """执行 Coupons 测试用例"""
    # 获取 Coupons 的测试用例数据
    excel = ReadExcel(test_case_path, "Coupons")
    coupon_test_data = excel.read_data_object()
    # 写测试结果的列数
    result_column = 11

    # 划分测试用例数据
    # 查询 coupon 正常的用例
    prepare_coupon_normal_data = []
    # 查询 coupon 异常的用例
    prepare_coupon_abnormal_data = []
    # 兑换 coupon 成功的用例
    redeem_coupon_normal_data = []
    # 兑换 coupon 异常的用例
    redeem_coupon_abnormal_data = []
    # 退还 coupon 正常的用例
    cancel_coupon_normal_data = []
    # 退还 coupon 异常的用例
    cancel_coupon_abnormal_data = []

    for data in coupon_test_data:
        if data.flow == "normal":
            if data.interface == "prepareCoupons":
                prepare_coupon_normal_data.append(data)
            elif data.interface == "redeemCoupons":
                redeem_coupon_normal_data.append(data)
            elif data.interface == "cancelCoupons":
                cancel_coupon_normal_data.append(data)
        elif data.flow == "abnormal":
            if data.interface == "prepareCoupons":
                prepare_coupon_abnormal_data.append(data)
            elif data.interface == "redeemCoupons":
                redeem_coupon_abnormal_data.append(data)
            elif data.interface == "cancelCoupons":
                cancel_coupon_abnormal_data.append(data)
        elif data.flow == "skip":
            excel.write_data(row=data.case_id + 1, column=result_column, value="Skip", font_color=colors.PURPLE)

    @allure.story("查询 coupon 正常")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("{test_data.title}")
    # @pytest.mark.skip
    @pytest.mark.parametrize("test_data", prepare_coupon_normal_data[0:1])
    def test_prepare_coupon_normal(self, test_data, get_session, get_auth):
        """测试查询 coupon 正常的用例"""
        case_id, interface, flow, title, method, url, params, headers, data, expected, check_sql = get_test_data(
            test_data)
        # 发送请求
        response = http.send(url=url, method=method, params=params, data=data, headers=headers)
        my_logger.info(response.url)
        my_logger.info(headers)
        my_logger.info(response.status_code)
        my_logger.info("data:{}".format(data))
        my_logger.info(response.json())

    @allure.story("查询 coupon 异常")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("{test_data.title}")
    @pytest.mark.skip
    @pytest.mark.parametrize("test_data", prepare_coupon_abnormal_data)
    def test_prepare_coupon_abnormal(self, test_data):
        """测试查询 coupon 异常的用例"""
        case_id, interface, flow, title, method, url, params, headers, data, expected, check_sql = get_test_data(
            test_data)
        pass

    def test_redeem_coupon_normal(self, test_data):
        """测试兑换 coupon 正常的用例"""
        pass

    def test_redeem_coupon_abnormal(self, test_data):
        """测试兑换 coupon 异常的用例"""
        pass

    def test_cancel_coupon_normal(self, test_data):
        """测试退还 coupon 正常的用例"""
        pass

    def test_cancel_coupon_abnormal(self, test_data):
        """测试退还 coupon 异常的用例"""
        pass


    # def test_de(self,get_auth):
    #     my_logger.info("test")

if __name__ == '__main__':
    pytest.main(["-s"])
