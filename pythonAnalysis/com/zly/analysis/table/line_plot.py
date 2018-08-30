#_author:"zhengly"
#date:2018/8/30
'''
折线图
'''
from numpy.random import randn
import matplotlib.pyplot as plt
plt.style.use('ggplot')
#随机数
plot_data1 = randn(50).cumsum()
plot_data2 = randn(50).cumsum()
plot_data3 = randn(50).cumsum()
plot_data4 = randn(50).cumsum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
#创建四条折线
ax1.plot(plot_data1,marker=r'o',color=u'blue',linestyle='-',label='Blue Solid')
ax1.plot(plot_data2,marker=r'+',color=u'red',linestyle='-',label='Red Dashed')
ax1.plot(plot_data3,marker=r'*',color=u'green',linestyle='-',label='Green Dash Dot')
ax1.plot(plot_data4,marker=r's',color=u'orange',linestyle='-',label='Orange Dotted')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title('Line Plots:Markers,Color,and Linestyles')
plt.xlabel('Draw')
plt.ylabel('Random Number')
#loc='best'指示matplotlib根据图中的空白部分将图例放在最合适的位置
plt.legend(loc='best')
plt.savefig('line_plot.png',dpi=400,bbox_inches='tight')
plt.show()