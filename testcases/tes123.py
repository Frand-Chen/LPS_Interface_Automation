# -*- coding=utf-8 -*-
import json
import pytest

from common.read_excel import ReadExcel
from testcases import *
excel = ReadExcel(test_case_path, "Session")
session_test_data = excel.read_data_object()
# 写测试结果的列数
result_column = 10

get_session_normal_data = []
get_session_abnormal_data = []
delete_session_normal_data = []
delete_session_abnormal_data = []

for data in session_test_data:
    if data.interface == "getSession":
        if data.flow == "normal":
            get_session_normal_data.append(data)
        elif data.flow == "abnormal":
            get_session_abnormal_data.append(data)
    elif data.interface == "deleteSession":
        if data.flow == "normal":
            delete_session_normal_data.append(data)
        elif data.flow == "abnormal":
            delete_session_abnormal_data.append(data)

print(len(get_session_normal_data))
print(len(get_session_abnormal_data))
print(len(delete_session_normal_data))
print(len(delete_session_abnormal_data))