#_author:"zhengly"
#date:2018/7/1
'''
利用sqlites模块创建数据库，读取CSV文件数据，并插入到创建好的数据库,然后更新已经存在的数据
'''
import sqlite3
import csv
input_file = "E:\\studytest\\data\\database\\data_for_updating.csv"
#创建数据库
con = sqlite3.connect('E:\\studytest\\data\\excel_test\\data.db')
#创建表语句
query="""CREATE TABLE sales (customer VARCHAR(20),product VARCHAR(40),amount FLOAT,date DATE);"""
#执行语句
con.execute(query)
#提交语句
con.commit()

#在表中插入数据
data = [('Richard Lucas','Notepad',2.50,'2014-01-02'),
        ('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
        ('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
        ('Steohen Randolph', 'Computer', 679.40, '2014-02-20')]
for tuple in data:
    print(tuple)
statement = "INSERT INTO sales VALUES(?,?,?,?)"
#执行多次插入语句
con.executemany(statement,data)
con.commit()
#读取CSV文件并更新特定行
file_reader = csv.reader(open(input_file,'r'),delimiter=',')
header=next(file_reader,None)
for row in file_reader:
    #封装每行数据
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    con.execute("UPDATE sales SET amount=?,date=? WHERE customer=?;",data)
con.commit()
#查询sales表
cursor = con.execute("SELECT * FROM sales");
rows = cursor.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(row[column_index])
    print(output)