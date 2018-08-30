#_author:"zhengly"
#date:2018/8/30
'''
除了使用matplotlib创建标准统计图，还可以使用panda来创建其他类型的统计图
本例实现：利用panda创建一个条形图和箱线图，并将它们并排放置
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
fig,axes=plt.subplots(nrows=1,ncols=2)
ax1,ax2 = axes.ravel()
data_frame = pd.DataFrame(np.random.rand(5,3),index=['Customer 1','Customer 2','Customer 3','Customer 4','Customer 5'],
                          columns=pd.Index(['Metric 1','Metric 2','Metric 3'],name='Metric'))
data_frame.plot(kind='bar',ax=ax1,alpha=0.75,title='Bar Plot')
plt.setp(ax1.xticks(),rotation=45,fontsize=10)