# -*- coding=utf-8 -*-
import os

from common.contents import DATA_DIR
from common.handle_config import gen_conf

# 获取测试用例文件
test_case_file = gen_conf.get("testdata", "test_case_file")
test_case_path = os.path.join(DATA_DIR, test_case_file)
