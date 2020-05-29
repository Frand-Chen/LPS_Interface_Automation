# -*- coding=utf-8 -*-

"""
session 测试用例模块
"""

import pytest
import os

from common.contents import DATA_DIR
from common.handle_config import gen_conf

# 获取测试用例数据
from common.read_excel import ReadExcel

test_case_file = gen_conf.get("testdata", "test_case_file")
test_case_path = os.path.join(DATA_DIR, test_case_file)
excel = ReadExcel(test_case_path, "Session")
session_test_data = excel.read_data_object()

class TestSession:

    @pytest.mark.parametrize("test_info",session_test_data)
    def test_session(self):

