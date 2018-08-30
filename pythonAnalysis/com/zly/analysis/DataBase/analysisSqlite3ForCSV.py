#_author:"zhengly"
#date:2018/7/1
'''
利用sqlites模块创建数据库，读取CSV文件数据，并插入到创建好的数据库
'''
import sqlite3
import csv
import sys
input_file = "E:\\studytest\\data\\csv\\supplier_data.csv"
#创建数据库
con = sqlite3.connect('E:\\studytest\\data\\excel_test\\Suppliers.db')
c = con.cursor()
#创建表语句
creat_table="""CREATE TABLE IF NOT EXISTS Suppliers (Supplier_Name VARCHAR(20),
          Invoice_Number VARCHAR(40),Part_Number VARCHAR(20),Cost FLOAT,Purchase_Date DATE);"""
#执行语句
c.execute(creat_table)
#提交语句
con.commit()

#读取CSV文件数据，并插入到数据库
file_reader = csv.reader(open(input_file,'r'),delimiter=',')
header=next(file_reader,None)
for row in file_reader:
    #封装每行数据
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    c.execute("INSERT INTO Suppliers VALUES(?,?,?,?,?);",data)
con.commit()
print("")
#查询Suppliers表
output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(row[column_index])
    print(output)