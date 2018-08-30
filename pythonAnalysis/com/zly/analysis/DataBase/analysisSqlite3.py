#_author:"zhengly"
#date:2018/7/1
'''
利用sqlites模块创建数据库，并插入数据，查询数据
'''
import sqlite3
#创建数据库
con = sqlite3.connect('E:\\studytest\\data\\excel\\data.db')
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
statement = "INSERT INTO sales VALUES(?,?,?,?)"
#执行多次插入语句
con.executemany(statement,data)
con.commit()

#查询sales表
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()

#计算查询结果中行的数量
row_counter = 0
for row in rows:
    print(row)
    row_counter += 1
print('Number of rows:%d'%(row_counter))