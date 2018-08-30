#_author:"zhengly"
#date:2018/8/30
'''
散点图
'''
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
x = np.arange(start=1.,stop=15.,step=1.)
#两条线
y_liner = x + 5. * np.random.randn(14)
y_quadratic = x**2 + 10.*np.random.randn(14)
#使用polyfit函数通过两组数据点拟合出一条直线和一条二次曲线
#再使用polyld函数根据直线和二次曲线的参数生成一个线形方程和二次方程
fn_liner = np.poly1d(np.polyfit(x,y_liner,deg=1))
fn_quadratic = np.poly1d(np.polyfit(x,y_quadratic,deg=2))
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
#'bo'蓝色圆圈，'go'绿色圆圈，'b-'蓝色实线，'g-'绿色实线,linewidth线的宽度
ax1.plot(x,y_liner,'bo',x,y_quadratic,'go',x,fn_liner(x),'b-',x,fn_quadratic(x),'g-',linewidth=2.)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title('Scatter Plots Regression Lines')
plt.xlabel('x')
plt.ylabel('f(x)')
#设置X轴和Y轴的范围
plt.xlim(min(x)-1.,max(x)+1.)
plt.ylim((min(y_quadratic)-10.,max(y_quadratic)+10.))
plt.savefig('scatter_plot.png',dpi=400,bbox_inches='tight')
plt.show()