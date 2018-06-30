#_author:"zhengly"
#date:2018/6/29
import sys
from xlrd import open_workbook
'''
利用xlrd模块读取excel工作簿三个表的name，行数和列数
'''
input_file="E:\\studytest\\data\\excel\\sales_2013.xlsx"
workbook=open_workbook(input_file)
print("Number of worksheets:",workbook.nsheets)
for worksheet in workbook.sheets():
    print("Worksheet name:",worksheet.name,"\tRows:",worksheet.nrows,"\tColumns:",worksheet.ncols)