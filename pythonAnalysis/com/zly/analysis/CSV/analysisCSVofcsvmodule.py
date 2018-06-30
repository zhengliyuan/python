#_author:"zhengly"
#date:2018/6/28
'''
利用python中csv模块是实现读写csv文件
'''
import sys
import csv
input_file='E:\\studytest\\checking.csv'
output_file='E:\\studytest\\checking11122.csv'
# input_file=sys.argv[1]
# output_file=sys.argv[2]

with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader=csv.reader(csv_in_file,delimiter=',')#将csv文件的每行以列表的形式返回
        filewriter=csv.writer(csv_out_file,delimiter=',')#创建一个写入对象，delimiter是默认分隔符
        for row_list in filereader:
            print(row_list)
            filewriter.writerow(row_list)
