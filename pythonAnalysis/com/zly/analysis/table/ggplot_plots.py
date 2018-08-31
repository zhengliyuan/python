#_author:"zhengly"
#date:2018/8/31
'''
使用ggplot创建统计图
必须使用ggplot2版本
'''
from ggplot import *
print(mtcars.head())
plt1 = ggplot(aes(x='mpg'),data=mtcars)+\
        geom_histogram(fill='darkblue',binwudth=2)+\
        xlim(10,35)+ylim(0,10)+\
        xlab('MPG')+ylab('Frequency')+\
        ggtitle('Histogram of MPG')