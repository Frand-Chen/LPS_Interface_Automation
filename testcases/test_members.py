# -*- coding=utf-8 -*-

"""
members 测试用例模块
"""
import os

import pytest

# 获取测试用例文件
from jsonpath import jsonpath
from openpyxl.styles import colors

from common.contents import DATA_DIR
from common.handle_config import gen_conf, sec_conf
from common.handle_data import get_test_data, TestData
from common.handle_request import handle_session_request as http
from common.logger import my_logger
from common.read_excel import ReadExcel

test_case_file = gen_conf.get("testdata", "test_case_file")
test_case_path = os.path.join(DATA_DIR, test_case_file)


class TestMembers:
    """执行 Members 测试用例"""
    # 获取 Members 的测试用例数据
    excel = ReadExcel(test_case_path, "Members")
    members_test_data = excel.read_data_object()
    # 写测试结果的列数
    result_column = 10

    # @pytest.mark.skip
    @pytest.mark.parametrize("test_data", members_test_data[0:1])
    def test_members_normal(self, test_data, get_session):
        """测试 members 请求正常的用例"""
        if test_data.interface == "Members" and test_data.flow == "normal":
            # 测试数据
            case_id, interface, flow, title, method, url, params, headers, data, expected, check_sql = get_test_data(
                test_data)
            headers["Host"] = sec_conf.get("environment", "host")
            headers["AKey"] = sec_conf.get("environment", "Akey")
            headers["Session"] = getattr(TestData, "seesionId")
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


if __name__ == '__main__':
    pytest.main(["-s"])
