"""
1.读取excel表格
2.读取出来的数据格式[{},{}]
3.处理单元格中的数据格式
    在excel中各种数据类型都有对应编号 ctype
    ctype      数据类型
    2           int
    3           date
    4           Boolean
"""
import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime


class OperationExcel(object):
    def __init__(self,filename,index = 0):
        """
        打开并按照索引去读取表格
        :param filename: 文件名/文件路径
        :param index: 需要读取的表格索引值
        :return:
        """
        # 打开excel文件
        table = xlrd.open_workbook(filename=filename)
        # 通过索引读取具体表格
        self.sheet = table.sheet_by_index(index)

    def read_excel_data(self):
        """
        读取表格中的数据,并对特殊数据进行处理
        通过按照读取单元格的数据,对单元格的数据进行数据类型转换
        :return:
        """
        # 得到表格行数和列数
        rows = self.sheet.nrows # 总行数
        cols = self.sheet.ncols # 总列数
        # 遍历行和列得到单元格的数据(先遍历行,再遍历列)
        all_data_list = []
        for row in range(1,rows):
            cell_data_list = []
            for col in range(cols):
                cell = self.sheet.cell_value(row,col) # 得到单元格数据
                ctype = self.sheet.cell(row,col).ctype # 得到单元格的数据类型
                if ctype == 2 and cell % 1 == 0: # 说明单元格数据类型是整数
                    cell = int(cell)
                elif ctype == 3: # 说明单元格的数据类型是日期
                    date = datetime(*xldate_as_tuple(cell,0))
                    print(date)
                    cell = date.strftime("%Y_%m_%d %H_%M_%S")
                elif ctype == 4:
                    cell = True if cell == 1 else False # 三目运算符
                cell_data_list.append(cell)
            all_data_list.append(cell_data_list)

        return all_data_list

    def get_data_for_dict(self):
        """
        将表格中的数据按照[{},{}]格式输出
        :return:
        """
        keys = self.sheet.row_values(0) # 将表格的第一行作为字典的键
        values = self.read_excel_data() # 将表格中剩余的行作为字典的值
        data_list = []
        for value in values:
            tmp = zip(keys,value)
            data_list.append(dict(tmp))
        return data_list


if __name__ == '__main__':
    oper = OperationExcel('testdata.xlsx')
    data = oper.read_excel_data()
    # data = oper.get_data_for_dict()
    print(data)