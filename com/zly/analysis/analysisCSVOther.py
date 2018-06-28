#_author:"zhengly"
#date:2018/6/28
import sys
import csv
'''
选取连续的行
'''
# input_file='E:\\studytest\\data.csv'
# output_file='E:\\studytest\\data_other1.csv'
# row_counter = 0
# with open(input_file,'r',newline='') as csv_in_file:
#     with open(output_file,'w',newline='') as csv_out_file:
#         filereader=csv.reader(csv_in_file)
#         filewriter=csv.writer(csv_out_file)
#         for row in filereader:
#             if row_counter >= 3 and row_counter <= 15:
#                 filewriter.writerow([value.strip() for value in row])
#             row_counter += 1
'''
添加标题行
'''
# input_file='E:\\studytest\\data_notitle.csv'
# output_file='E:\\studytest\\data_other2.csv'
# with open(input_file,'r',newline='') as csv_in_file:
#     with open(output_file,'w',newline='') as csv_out_file:
#         filereader=csv.reader(csv_in_file)
#         filewriter=csv.writer(csv_out_file)
#         header_list = ['Title1','Title2','Title3','Title4','Title5']
#         filewriter.writerow(header_list)
#         for row in filereader:
#             filewriter.writerow(row)

'''
读取多个CSV文件
1、文件记数和行列记数
'''
import glob
import os
#存放多个文件的文件夹目录，文件命令格式相似
# input_path='E:\\studytest\\multile'
# file_counter = 0
# #循环文件夹中所有文件
# for input_file in  glob.glob(os.path.join(input_path,'data*')):
#     row_counter = 1
#     with open(input_file,'r',newline='') as csv_in_file:
#         filereader = csv.reader(csv_in_file)
#         header=next(filereader,None)
#         for row in filereader:
#             row_counter += 1
#     print('{0!s}:\t{1:d} rows \t{2:d} columns'.format(os.path.basename(input_file),row_counter,len(header)))
#     file_counter += 1;
# print('Number of files:{0:d}'.format(file_counter))
'''
2、将多个文件的数据放到一个文件中
'''
# input_path='E:\\studytest\\multile'
# output_file='E:\\studytest\\multile\\count_data.csv'
# first_file = True
# for input_file in glob.glob(os.path.join(input_path,'data*')):
#     print(os.path.basename(input_file))
#     with open(input_file,'r',newline='') as csv_in_file:
#         with open(output_file,'a',newline='') as  csv_out_file:
#             filereader = csv.reader(csv_in_file)
#             filewriter = csv.writer(csv_out_file)
#             #如果是第一次，就全部添加
#             if first_file:
#                 for row in filereader:
#                     filewriter.writerow(row)
#                 first_file = False
#             #如果不是第一次，只添加除了标题外的其他行
#             else:
#                 header = next(filereader,None)
#                 for row in filereader:
#                     filewriter.writerow(row)

'''
3、计算每个文件中值的总和和平均数
'''
input_path='E:\\studytest\\multile'
output_file='E:\\studytest\\multile\\count_average_data.csv'
#构造结果文件的标题列
output_header_list=['file_name','total_sales','average_sales']
csv_out_file=open(output_file,'a',newline='')
filewriter=csv.writer(csv_out_file)
filewriter.writerow(output_header_list)
#循环文件夹中每个文件
for input_file in glob.glob(os.path.join(input_path,'data*')):
    with open(input_file,'r',newline='') as csv_in_file:
        #读取文件
        filereader = csv.reader(csv_in_file)
        #构造插入数据格式['file_name','total_sales','average_sales']
        output_list=[]
        #插入文件名
        output_list.append(os.path.basename(input_file))
        header = next(filereader)
        total_sales = 0.0
        number_of_sales = 0.0
        #循环除标题行的每一行
        for row in filereader:
            #获得总销售额
            sale_count = row[3]
            total_sales += float(str(sale_count).strip('$').replace(',',''))
            #获取销售条数
            number_of_sales += 1
        #获取平均销售额
        average_sales = '{0:.2f}'.format(total_sales / number_of_sales)
        #插入总销售额
        output_list.append(total_sales)
        #插入平均销售额
        output_list.append(average_sales)
        #插入结果问价
        filewriter.writerow(output_list)
csv_out_file.close()
