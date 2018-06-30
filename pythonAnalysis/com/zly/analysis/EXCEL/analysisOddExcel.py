#_author:"zhengly"
#date:2018/6/30
import sys
from xlrd import open_workbook,xldate_as_tuple
from xlwt import Workbook
'''
处理单个工作表
1、读写excel文件
'''
# input_file='E:\\studytest\\data\\excel\\sales_2013.xlsx'
# output_file='E:\\studytest\\data\\excel_test\\2output.xlsx'
# output_workbook=Workbook()
# output_worksheet=output_workbook.add_sheet('jan_2013_output')
# with open_workbook(input_file) as workbook:
#     #根据工作表名字选区工作表
#     worksheet=workbook.sheet_by_name('january_2013')
#     for row_index in range(worksheet.nrows):
#         for column_index in range(worksheet.ncols):
#             output_worksheet.write(row_index,column_index,worksheet.cell_value(row_index,column_index))
# output_workbook.save(output_file)
'''
需要注意的问题：假如工作表中存在日期，在写的时候会变成该日期和1900年1月1日之间的天数差，所以
如果工作表中存在日期，在写的时候需要利用date模块对该列进行格式化
'''
# from datetime import date
# input_file='E:\\studytest\\data\\excel\\sales_2013.xlsx'
# output_file='E:\\studytest\\data\\excel_test\\2output_date.xlsx'
# output_workbook=Workbook()
# output_worksheet=output_workbook.add_sheet('jan_2013_output')
# with open_workbook(input_file) as workbook:
#     worksheet=workbook.sheet_by_name('january_2013')
#     #循环行
#     for row_index in range(worksheet.nrows):
#         #用于存放构造好的行数据
#         row_list_output = []
#         #循环列
#         for column_index in range(worksheet.ncols):
#             #type=3表示该列类型为日期
#             #若该列为日期格式，则格式化日期
#             if worksheet.cell_type(row_index,column_index) == 3:
#                 date_cell = xldate_as_tuple(worksheet.cell_value(row_index,column_index),workbook.datemode)
#                 date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
#                 row_list_output.append(date_cell)
#                 output_worksheet.write(row_index,column_index,date_cell)
#             #否则直接拼接row_list_output
#             else:
#                 non_date_cell = worksheet.cell_value(row_index,column_index)
#                 row_list_output.append(non_date_cell)
#                 output_worksheet.write(row_index,column_index,non_date_cell)
# output_workbook.save(output_file)
'''
# 2、筛选特定行
#  2、1 行中的值满足某个条件
#  2、2 行中的值属于某个集合（和上面的差不多，判断条件改成in A集合）
#  2、3 行中的值匹配于特定的模式（和上面的差不多，判断条件改成pattern.search（数值））
# '''
# from datetime import date
# input_file='E:\\studytest\\data\\excel\\sales_2013.xlsx'
# output_file='E:\\studytest\\data\\excel_test\\4output.xlsx'
# output_workbook=Workbook()
# output_worksheet=output_workbook.add_sheet('jan_2013_output')
# #条件：第四列的值
# sale_amount_column_index=3
# with open_workbook(input_file) as workbook:
#     worksheet=workbook.sheet_by_name('january_2013')
#     data = []
#     #取表头
#     header = worksheet.row_values(0)
#     data.append(header)
#     #循环第1行到最后一行
#     for row_index in range(1,worksheet.nrows):
#         #用于存放构造好的行数据
#         row_list_output = []
#         #取出需要判断列的值，比如某列值大于1400
#         sale_amount = worksheet.cell_value(row_index,sale_amount_column_index)
#         if sale_amount > 1400.0:
#             #循环该列
#             for column_index in range(worksheet.ncols):
#                 #type=3表示该列类型为日期
#                 #若该列为日期格式，则格式化日期
#                 if worksheet.cell_type(row_index,column_index) == 3:
#                     date_cell = xldate_as_tuple(worksheet.cell_value(row_index,column_index),workbook.datemode)
#                     date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
#                     row_list_output.append(date_cell)
#                 #否则直接拼接row_list_output
#                 else:
#                     non_date_cell = worksheet.cell_value(row_index,column_index)
#                     row_list_output.append(non_date_cell)
#             if row_list_output:
#                 data.append(row_list_output)
#     #此处用迭代的原因是因为，如果直接写入的话，会导致索引也写入到新文件中，写入后的文件会出现空白行的情况
#     for list_index,output_list in enumerate(data):
#         for element_index,element in enumerate(output_list):
#             output_worksheet.write(list_index,element_index,element)
# output_workbook.save(output_file)
'''
3、选取特定的列
 3、1 根据列索引值
'''
# from datetime import date
# input_file='E:\\studytest\\data\\excel\\sales_2013.xlsx'
# output_file='E:\\studytest\\data\\excel_test\\7output.xlsx'
# output_workbook=Workbook()
# output_worksheet=output_workbook.add_sheet('jan_2013_output')
# #条件：只取索引号为1和4的两列
# my_columns = [1,4]
# with open_workbook(input_file) as workbook:
#     worksheet=workbook.sheet_by_name('january_2013')
#     data = []
#     for row_index in range(worksheet.nrows):
#         #用于存放构造好的行数据
#         row_list = []
#         #循环满足条件的列
#         for column_index in my_columns:
#             cell_value = worksheet.cell_value(row_index,column_index)
#             cell_type = worksheet.cell_type(row_index,column_index)
#             #type=3表示该列类型为日期
#             #若该列为日期格式，则格式化日期
#             if cell_type == 3:
#                 date_cell = xldate_as_tuple(cell_value,workbook.datemode)
#                 date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
#                 row_list.append(date_cell)
#             #否则直接拼接row_list_output
#             else:
#                 row_list.append(cell_value)
#         data.append(row_list)
#     #此处用迭代的原因是因为，如果直接写入的话，会导致索引也写入到新文件中，写入后的文件会出现空白行的情况
#     for list_index,output_list in enumerate(data):
#         for element_index,element in enumerate(output_list):
#             output_worksheet.write(list_index,element_index,element)
# output_workbook.save(output_file)
'''
 3、2 根据列标题选取（同上，先根据标题选出列索引值，然后再使用列索引值）
'''
from datetime import date
input_file='E:\\studytest\\data\\excel\\sales_2013.xlsx'
output_file='E:\\studytest\\data\\excel_test\\8output.xlsx'
output_workbook=Workbook()
output_worksheet=output_workbook.add_sheet('jan_2013_output')
#条件：只取索引号为1和4的两列
my_columns = ['Customer ID','Purchase Date']
with open_workbook(input_file) as workbook:
    worksheet=workbook.sheet_by_name('january_2013')
    data = [my_columns]
    #取出列标题行
    header_list=worksheet.row_values(0)
    header_index_list = []
    #循环标题列表，找出符合条件列的索引号
    for header_index in range(len(header_list)):
        if header_list[header_index] in my_columns:
            header_index_list.append(header_index)
    for row_index in range(1,worksheet.nrows):
        #用于存放构造好的行数据
        row_list = []
        #循环满足条件的列
        for column_index in header_index_list:
            cell_value = worksheet.cell_value(row_index,column_index)
            cell_type = worksheet.cell_type(row_index,column_index)
            #type=3表示该列类型为日期
            #若该列为日期格式，则格式化日期
            if cell_type == 3:
                date_cell = xldate_as_tuple(cell_value,workbook.datemode)
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                row_list.append(date_cell)
            #否则直接拼接row_list_output
            else:
                row_list.append(cell_value)
        data.append(row_list)
    #此处用迭代的原因是因为，如果直接写入的话，会导致索引也写入到新文件中，写入后的文件会出现空白行的情况
    for list_index,output_list in enumerate(data):
        for element_index,element in enumerate(output_list):
            output_worksheet.write(list_index,element_index,element)
output_workbook.save(output_file)