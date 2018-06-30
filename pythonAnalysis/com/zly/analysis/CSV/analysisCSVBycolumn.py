#_author:"zhengly"
#date:2018/6/28
'''
利用python中csv模块读写文件(筛选特定的列)
'''
import sys
import csv
input_file='E:\\studytest\\data.csv'
output_file='E:\\studytest\\data_column.csv'
# input_file=sys.argv[1]
# output_file=sys.argv[2]
'''第一种：根据列索引值选出特定的列'''
# my_columns = [0,3]#限定我们需要的特定列
# with open(input_file,'r',newline='') as csv_in_file:
#     with open(output_file,'w',newline='') as csv_out_file:
#         filereader=csv.reader(csv_in_file)#将csv文件的每行以列表的形式返回
#         filewriter=csv.writer(csv_out_file)#创建一个写入对象，delimiter是默认分隔符
#         #处理所有行
#         for row_list in filereader:#循环每一行
#             row_list_output = []
#             for index_value in my_columns:
#                 row_list_output.append(row_list[index_value])#取出特定列的数据，并封装成列表
#             filewriter.writerow(row_list_output)#写入文件
'''第二种：根据列标题选出特定的列
        注：方法和第一种的区别在在于，先根据列标题找出列索引，然后在运用第一种方法读写文件，好处是列标题是固定的
'''
my_columns = ['Invoice Number','Purchase Date']
my_columns_index = []
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader=csv.reader(csv_in_file)#将csv文件的每行以列表的形式返回
        filewriter=csv.writer(csv_out_file)#创建一个写入对象，delimiter是默认分隔符
        header=next(filereader,None)
        for index_value in range(len(header)):
            if header[index_value] in my_columns:
                my_columns_index.append(index_value)
        filewriter.writerow(my_columns)
        for row_list in filereader:
            row_list_output = []
            for index_value in my_columns_index:
                row_list_output.append(row_list[index_value])
        filewriter.writerow(row_list_output)
