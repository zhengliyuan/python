#_author:"zhengly"
#date:2018/6/28
'''
利用python中csv模块读写文件(筛选特定的行)
    固定格式：
        for row in filereader:
            ***if value in row meets some business tule or set of rules:***
                do something
            else:
                do something else
'''
import sys
import csv
input_file='E:\\studytest\\data.csv'
output_file='E:\\studytest\\data111.csv'
# input_file=sys.argv[1]
# output_file=sys.argv[2]

with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader=csv.reader(csv_in_file)#将csv文件的每行以列表的形式返回
        filewriter=csv.writer(csv_out_file)#创建一个写入对象，delimiter是默认分隔符
        #先处理第一行
        header=next(filereader)
        filewriter.writerow(header)
        #再处理剩余所有行
        for row_list in filereader:
            supplier=str(row_list[0]).strip()
            cost=str(row_list[3]).strip("$").replace(',','')
            if supplier == 'Supplier Z' or float(cost)>600.00:
                filewriter.writerow(row_list)
