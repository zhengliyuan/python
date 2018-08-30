#_author:"zhengly"
#date:2018/7/1
'''
从CSV文件读取数据存入mysql
'''
import pymysql
import csv
import sys
from datetime import datetime,date
#CSV文件输入
input_file="E:\\studytest\\data\\csv\\supplier_data.csv"
#连接数据库
con = pymysql.connect(host='127.0.0.1',port=3306,db='my_suppliers',user='root',passwd='666666')
c =con.cursor()
#读取CSV文件数据插入到数据库中
file_reader = csv.reader(open(input_file,'r',newline=''))
header = next(file_reader)
for row in file_reader:
    data= []
    for column_index in range(len(header)):
        if column_index<4:
            data.append(str(row[column_index]).lstrip('$').replace(',','').strip())
        else:
            a_date = datetime.date(datetime.strptime(str(row[column_index]),'%m/%d/%y'))
            a_date = a_date.strftime('%Y-%m-%d')
            data.append(a_date)
    print(data)
    #执行插入语句
    c.execute("""INSERT INTO Suppliers VALUES(%s,%s,%s,%s,%s);""",data)
#提交事务
con.commit()
print("")
#查询Suppliers表
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)