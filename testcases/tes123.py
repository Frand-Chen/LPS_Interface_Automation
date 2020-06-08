# -*- coding=utf-8 -*-
import json
import pytest
from openpyxl.styles import colors
from common.read_excel import ReadExcel
from testcases import *

# excel = ReadExcel(test_case_path, "Session")
# session_test_data = excel.read_data_object()
# 写测试结果的列数
result_column = 11

excel = ReadExcel(test_case_path, "Members")
members_test_data = excel.read_data_object()

print("data个数:",len(members_test_data))

members_normal_data = []
members_abnormal_data = []
excel.write_data(row=2, column=result_column, value="Skip2", font_color=colors.PURPLE)
excel.write_data(row=3, column=result_column, value="Skip3", font_color=colors.PURPLE)
excel.write_data(row=4, column=result_column, value="Skip4", font_color=colors.PURPLE)

# for data in members_test_data:
#     if data.flow == "normal":
#         members_normal_data.append(data)
#         excel.write_data(row=data.case_id + 1, column=result_column, value="normal", font_color=colors.DARKGREEN)
#     elif data.flow == "abnormal":
#         members_abnormal_data.append(data)
#         excel.write_data(row=data.case_id + 1, column=result_column, value="abnormal", font_color=colors.RED)
#     elif data.flow == "skip":
#         print("flow: ", data.flow)
#         print("case_id: ", data.case_id)
#         excel.write_data(row=data.case_id + 1, column=result_column, value="Skip", font_color=colors.PURPLE)
#         excel.save()
#         print("写入数据 ")