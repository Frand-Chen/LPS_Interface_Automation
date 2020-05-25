# -*- coding=utf-8 -*-

"""
该模块用来操作 excel 测试用例文件(.xlsx格式)
"""
import openpyxl


class TestData:
    """保存测试用例数据"""
    pass


class ReadExcel:
    def __init__(self, file_name, sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name

    def open(self):
        """打开 excel，选择表单"""
        self.work_book = openpyxl.load_workbook(self.file_name)
        self.sheet = self.work_book[self.sheet_name]

    def read_data_dict(self) -> list:
        """
        读取测试用例数据，保存在 Dict 中
        :return: 列表嵌套 Dict
        """
        self.open()
        # 按行获取所有的单元格数据
        row_sheets = list(self.sheet.rows)
        # 获取表头行
        title = []
        for row in row_sheets[0]:
            title.append(row.value)
        # 遍历获取每条测试用例数据，并保存在 list 中
        cases = []
        for row in row_sheets[1:]:
            data = []
            for sheet in row:
                data.append(sheet.value)
            # 把每个 sheet 的数据以 Dict 保存
            data_dict = dict(zip(title,data))
            cases.append(data_dict)
        return cases


    def read_data_object(self):
        pass

    def save(self):
        pass

    def close(self):
        pass

    def write_data(self):
        pass


if __name__ == '__main__':
    data = ReadExcel(r"E:\CodeLibrary\LPS_Interface_Automation\data\LPS_testcases.xlsx", "Session")
    case = data.read_data_dict()
    print(len(case))
    for ele in case:
        print(ele)
