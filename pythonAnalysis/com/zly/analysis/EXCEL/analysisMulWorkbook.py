#_author:"zhengly"
#date:2018/6/30
'''
处理多个工作簿
1、工作表计数以及每个工作表中的行列计数
'''
# import glob
# import os
# import sys
# from xlrd import open_workbook
# input_directory = 'E:\\studytest\\data\\excel'
# workbook_counter = 0
# for input_file in glob.glob(os.path.join(input_directory,'*.xlsx')):
#     workbook = open_workbook(input_file)
#     print('Workbook:%s'%os.path.basename((input_file)))
#     print('Number of worksheets:%d'%workbook.nsheets)
#     for worksheet in workbook.sheets():
#         print('Worksheet name:',worksheet.name,'\tRows:',worksheet.nrows,'\tColumns:',worksheet.ncols)
#     workbook_counter += 1
# print('Number of Excel workbooks:%d'%(workbook_counter))
'''
2、从多个工作簿中连接数据
'''
# import glob
# import os
# import sys
# from datetime import date
# from xlrd import open_workbook,xldate_as_tuple
# from xlwt import Workbook
# input_directory = 'E:\\studytest\\data\\excel'
# output_file = 'E:\\studytest\\data\\excel_test\\13output.xlsx'
# output_workbook = Workbook()
# output_worksheet = output_workbook.add_sheet('all_data_all_workbooks')
# data = []
# first_worksheet = True
# #循环多个工作簿
# for input_file in glob.glob(os.path.join(input_directory,'*.xls*')):
#    print(os.path.basename(input_file))
#    #打开当前工作簿
#    with open_workbook(input_file) as workbook:
#        #循环当前工作簿的每个工作表
#        for worksheet in workbook.sheets():
#            if first_worksheet:
#                header_row = worksheet.row_values(0)
#                data.append(header_row)
#                first_worksheet = False
#             #循环行
#            for row_index in range(1,worksheet.nrows):
#                row_list = []
#                #循环列
#                for column_index in range(worksheet.ncols):
#                     cell_value = worksheet.cell_value(row_index,column_index)
#                     cell_type = worksheet.cell_type(row_index,column_index)
#                     if cell_type == 3:
#                         date_cell = xldate_as_tuple(cell_value,workbook.datemode)
#                         date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
#                         row_list.append(date_cell)
#                     else:
#                         row_list.append(cell_value)
#                data.append(row_list)
# for list_index,output_list in enumerate(data):
#     for element_index,element in enumerate(output_list):
#         output_worksheet.write(list_index,element_index,element)
# output_workbook.save(output_file)
'''
3、为每个工作簿和工作表计算总数和均值
'''
import glob
import os
import sys
from datetime import date
from xlrd import open_workbook,xldate_as_tuple
from xlwt import Workbook
input_directory = 'E:\\studytest\\data\\excel'
output_file = 'E:\\studytest\\data\\excel_test\\14output.xlsx'
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('sums_and_averages')
all_data = []
#对索引号为3的列求总值和平均值
sale_column_index = 3
#输出文件列标题
header = ['workbook','worksheet','worksheet_total','worksheet_average','workbook_total','workbook_average']
all_data.append(header)
#循环多个工作簿
for input_file in glob.glob(os.path.join(input_directory,'*.xls*')):
   #打开当前工作簿
   with open_workbook(input_file) as workbook:
       #存放当前工作簿所求列的总值
       list_of_totals = []
       # 存放当前工作簿所求列的个数
       list_of_number = []
       workbook_output = []
       #循环当前工作簿的每个工作表
       for worksheet in workbook.sheets():
           #当前工作表所求列总值
           total_sales = 0
           #当前工作表所求列个数
           number_of_sales = 0
           #存放当前工作表的名字，总值，平均值
           worksheet_list = []
           worksheet_list.append(os.path.basename(input_file))
           worksheet_list.append(worksheet.name)
            #循环行
           for row_index in range(1,worksheet.nrows):
               try:
                   total_sales += float(str(worksheet.cell_value(row_index,sale_column_index)))
                   number_of_sales += 1
               except:
                   total_sales += 0
                   number_of_sales += 0
           average_sales = '%.2f'%(total_sales/number_of_sales)
           worksheet_list.append(total_sales)
           worksheet_list.append(float(average_sales))
           list_of_totals.append(total_sales)
           list_of_number.append(float(average_sales))
           workbook_output.append(worksheet_list)
       workbook_total = sum(list_of_totals)
       workbook_average = sum(list_of_totals)/sum(list_of_number)
       for list_element in workbook_output:
           list_element.append(workbook_total)
           list_element.append(workbook_average)
       all_data.extend(workbook_output)

for list_index,output_list in enumerate(all_data):
    for element_index,element in enumerate(output_list):
        output_worksheet.write(list_index,element_index,element)
output_workbook.save(output_file)