#_author:"zhengly"
#date:2018/6/30
'''
读取工作簿中的所有工作表
1、在所有工作表中筛选特定行
'''
# import sys
# from datetime import date
# from xlrd import open_workbook,xldate_as_tuple
# from xlwt import Workbook
# input_file='E:\\studytest\\data\\excel\\sales_2013.xlsx'
# output_file='E:\\studytest\\data\\excel_test\\10output.xlsx'
# output_workbook=Workbook()
# output_worksheet=output_workbook.add_sheet('filtered_rows_all_worksheets')
# sale_column_index = 3
# threshold = 2000.0
# first_worksheet = True
# with open_workbook(input_file) as workbook:
#     data = []
#     for worksheet in workbook.sheets():
#         if first_worksheet:
#             header_row=worksheet.row_values(0)
#             data.append(header_row)
#             first_worksheet= False
#         for row_index in range(1,worksheet.nrows):
#             row_list = []
#             sale_amount=worksheet.cell_value(row_index,sale_column_index)
#             if sale_amount > threshold:
#                 for column_index in range(worksheet.ncols):
#                     cell_value = worksheet.cell_value(row_index,column_index)
#                     cell_type = worksheet.cell_type(row_index,column_index)
#                     if cell_type == 3:
#                         date_cell=xldate_as_tuple(cell_value,workbook.datemode)
#                         date_cell=date(*date_cell[0:3]).strftime('%m/%d/%Y')
#                         row_list.append(date_cell)
#                     else:
#                         row_list.append(cell_value)
#             if row_list:
#                 data.append(row_list)
#     for list_index,output_list in enumerate(data):
#         for element_index,element in enumerate(output_list):
#             output_worksheet.write(list_index,element_index,element)
# output_workbook.save(output_file)
'''
2、在所有工作表中筛选特定列
    根据前面操作单工作表的代码，我们可以发现这个地方存在两种方法，一是根据索引值；二是根据列标题。我们以第二种为例。
'''
# import sys
# from datetime import date
# from xlrd import open_workbook,xldate_as_tuple
# from xlwt import Workbook
# input_file='E:\\studytest\\data\\excel\\sales_2013.xlsx'
# output_file='E:\\studytest\\data\\excel_test\\10output.xlsx'
# output_workbook=Workbook()
# output_worksheet=output_workbook.add_sheet('selected_columns_all_worksheets')
# #条件，取列标题为XX的两列
# my_columns = ['Customer Name','Sale Amount']
# first_worksheet = True
# with open_workbook(input_file) as workbook:
#     data = [my_columns]
#     #存放列标题对应的索引值
#     index_of_cols_to_keep = []
#     for worksheet in workbook.sheets():
#         if first_worksheet:
#             header_row=worksheet.row_values(0)
#             for column_index in range(len(header_row)):
#                 if header_row[column_index] in my_columns:
#                     index_of_cols_to_keep.append(column_index)
#             first_worksheet= False
#         for row_index in range(1,worksheet.nrows):
#             row_list = []
#             for column_index in index_of_cols_to_keep:
#                 cell_value = worksheet.cell_value(row_index,column_index)
#                 cell_type = worksheet.cell_type(row_index,column_index)
#                 if cell_type == 3:
#                     date_cell=xldate_as_tuple(cell_value,workbook.datemode)
#                     date_cell=date(*date_cell[0:3]).strftime('%m/%d/%Y')
#                     row_list.append(date_cell)
#                 else:
#                     row_list.append(cell_value)
#             data.append(row_list)
#     for list_index,output_list in enumerate(data):
#         for element_index,element in enumerate(output_list):
#             output_worksheet.write(list_index,element_index,element)
# output_workbook.save(output_file)
'''
3、在excel工作簿中读取一组工作表
'''
import sys
from datetime import date
from xlrd import open_workbook,xldate_as_tuple
from xlwt import Workbook
input_file='E:\\studytest\\data\\excel\\sales_2013.xlsx'
output_file='E:\\studytest\\data\\excel_test\\11output.xlsx'
output_workbook=Workbook()
output_worksheet=output_workbook.add_sheet('set_of_worksheets')
#条件，取索引号为0和1的两个工作表
my_sheets = [0,1]
first_worksheet = True
with open_workbook(input_file) as workbook:
    data = []
    #循环工作簿中每个工作表
    for sheet_index in range(workbook.nsheets):
        #判断是否为需要处理的工作表
        if sheet_index in my_sheets:
            # 找到符合要求的工作表，并取出表内容
            worksheet = workbook.sheet_by_index(sheet_index)
            if first_worksheet:
                header_row=worksheet.row_values(0)
                data.append(header_row)
                first_worksheet= False
            for row_index in range(1,worksheet.nrows):
                row_list = []
                for column_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index,column_index)
                    cell_type = worksheet.cell_type(row_index,column_index)
                    if cell_type == 3:
                        date_cell=xldate_as_tuple(cell_value,workbook.datemode)
                        date_cell=date(*date_cell[0:3]).strftime('%m/%d/%Y')
                        row_list.append(date_cell)
                    else:
                        row_list.append(cell_value)
                if row_list:
                    data.append(row_list)
    for list_index,output_list in enumerate(data):
        for element_index,element in enumerate(output_list):
            output_worksheet.write(list_index,element_index,element)
output_workbook.save(output_file)