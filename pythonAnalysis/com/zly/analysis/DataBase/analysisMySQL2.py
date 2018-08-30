#_author:"zhengly"
#date:2018/7/5
'''
查询一个表并将输出写入CSV文件
'''
import csv
import pymysql
#输出文件
output_file="E:\\studytest\\data\\excel_test\\5output.csv"
#连接数据库
con =pymysql.connect(host='127.0.0.1',port=3306,db='my_suppliers',user='root',passwd='666666')
c = con.cursor()
#打开输出文件，写入标题
filewriter=csv.writer(open(output_file,'w',newline=''),delimiter=',')
header=['Supplier Name','Invoice Number','Part Number','Cost','Purchase Date']
filewriter.writerow(header)
#循环数据库，插入数据到输出文件
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    filewriter.writerow(row)