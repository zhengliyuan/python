#_author:"zhengly"
#date:2018/6/27
'''
利用python普通模块是实现读写csv文件
步骤1:取出A文件的第一行，去除空格，换行符等符号
步骤2：将A文件的第一行保存到一个列表中，然后写入到B文件中
步骤3：依次循环A文件后面的各行，然后写入到B文件中
'''
import sys
input_file='E:\\studytest\\checking.csv'
output_file='E:\\studytest\\checking111.csv'

with open(input_file,'r',newline='') as  filereader:
    with open(output_file,'w',newline='') as filewrite:
        header=filereader.readline()
        header=header.strip()
        header_list=header.split(',')
        print(header_list)
        filewrite.write(','.join(map(str,header_list))+'\n')
        for row in filereader:
            row=row.strip()
            row_list=row.split(',')
            print(row_list)
            filewrite.write(','.join(map(str,row_list))+'\n')
