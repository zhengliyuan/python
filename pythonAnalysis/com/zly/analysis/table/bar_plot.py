#_author:"zhengly"
#date:2018/8/30
'''
条形图
'''
import matplotlib.pyplot as plt
#使用ggplot样式来模拟ggplot2风格的图形，ggplot2是一个常用的R语言绘图包
plt.style.use('ggplot')
customers = ['ABC','DEF','GHI','JKL','MNO']
customers_index = range(len(customers))
sale_amounts = [127,90,201,111,232]
#基础图
fig = plt.figure()
#在基础图上加上子图
ax1 = fig.add_subplot(1,1,1)
#param1:设置条形左侧在X轴上的坐标；param2:设置条形的高度;param3:设置条形和标签中间对齐；param4:设置条形的颜色
ax1.bar(customers_index,sale_amounts,align='center',color='darkblue')
#设置X,Y轴刻度线位置
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
#将条形的刻度线标签由客户索引值更改为实际的客户名称
plt.xticks(customers_index,customers,rotation=0,fontsize='small')
#设置X轴标签
plt.xlabel('Customer Name')
#设置Y轴标签
plt.ylabel('Sale Name')
#设置图标签
plt.title('Sale Amount per Customer')
#将统计图保存在当前文件夹，dpi为分辨率,bbox_inches将图形四周的空白部分去掉
plt.savefig('bar_plot.png',dpi=400,bbox_inches='tight')
#显示图形
plt.show()
