# -*- coding=utf-8 -*-

import os

import pytest
import time
# ts = str(int(time.time()))

# 报告一，生成 allure 报告
# 执行pytest单元测试，生成 Allure 报告需要的数据存在 allure_data 目录
pytest.main(["-s"])
# 执行命令 allure generate ./result -o ./report --clean ，生成测试报告
os.system('allure generate ./report/allure_data -o ./allure_report_html --clean')

# 报告二，生成 html 报告
# pytest.main(['-m test', '-s',"--html=report/report_{}.html".format(ts)])