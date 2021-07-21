# -*- coding=utf-8 -*-
import os

import pytest
# import time
#
# ts = str(int(time.time()))

# 接口测试开始执行命令
# pytest.main(["-s", "--allure-severities=critical,normal"])
# pytest.main(["-s", "-m","normal,abnormal"])
# pytest.main(["-sq", "--emoji"])
pytest.main(["-s",])

# 报告一，生成 allure 报告
# 生成 Allure 报告需要的数据存在 allure_report_data 目录
# os.system('allure generate ./allure_report_data -o ./allure_report_html --clean')
os.system(r'allure generate ./allure_report_data -o ./allure_report_html --clean')
# 运行完后自动打开报告
# os.system('allure open allure_report_html')