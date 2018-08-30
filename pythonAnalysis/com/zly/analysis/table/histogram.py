#_author:"zhengly"
#date:2018/8/30
'''
直方图
'''
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
mu1,mu2,sigma=100,130,15
#随机生成两个正态分布变量X1和X2，X1的均值为100，X2的均值为130
x1 = mu1+sigma*np.random.randn(10000)
x2 = mu2+sigma*np.random.randn(10000)
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
#创建两个柱状图
#bins表示被分割成50份，normed=False表示直方图显示的是频率分布，而不是概率分布，alpha=0.5表示透明度
n,bins,patches=ax1.hist(x1,bins=50,density=False,color='darkgreen')
n,bins,patches=ax1.hist(x2,bins=50,density=False,color='orange',alpha=0.5)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xlabel('Bins')
plt.ylabel('Number of Values in Bin')
#为基础图设置一个标题
fig.suptitle('Histogram',fontsize=14,fontweight='bold')
#为子图设置一个标题
ax1.set_title('Two Frequency Distributions')
plt.savefig('histogram.png',dpi=400,bbox_inches='tight')
plt.show()