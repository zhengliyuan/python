#_author:"zhengly"
#date:2018/8/31
'''
分析葡萄酒质量数据集
'''
print("*********************First************************")
'''
1、计算出每列的总体描述性统计量、质量列中的唯一值以及和这个唯一值对应的观测值
'''
input_file='E:\\studytest\\data\\statistics\\winequality-both.csv'
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols,glm
#将数据集读入到pandas数据框中
wine=pd.read_csv(input_file,sep=',',header=0)
print(wine.quality.unique())
#wine.columns=wine.columns.str.replace('','_')
print(wine.head())
#显示所有变量的描述性统计量(总数，均值，标准差，最小值，第25个百分位数，中位数，第75个百分位数，最大值)
print(wine.describe())
#找出唯一值
print(sorted(wine.quality.unique()))
#计算值的频率
print(wine.quality.value_counts())
print("*********************Second************************")
'''
2、分组分析红葡萄酒数据和白葡萄酒数据
'''
#按照葡萄类型显示质量的描述性统计量
print(wine.groupby('type')[['quality']].describe().unstack('type'))
#按照葡萄酒类型显示质量的特定分位数
print(wine.groupby('type')[['quality']].quantile([0.25,0.75]).unstack('type'))
#按照葡萄酒类型查看质量分布
red_wine = wine.loc[wine['type']=='red','quality']
white_wine = wine.loc[wine['type']=='white','quality']
sns.set_style("dark")
print(sns.distplot(red_wine,norm_hist=True,kde=False,color="red",label="Red wine"))
print(sns.distplot(white_wine,norm_hist=True,kde=False,color="white",label="White wine"))
#sns.axlabel("Quality Score","Density")
plt.title("Distribution of Quality by Wine Type")
plt.legend()
plt.show()
#检验红葡萄酒和白葡萄酒的平均质量是否相同
print(wine.groupby(['type'])[['quality']].agg(['std']))
#进行t检验
tstat,pvalue,df = sm.stats.ttest_ind(red_wine,white_wine)
print('tstat:%.3f pvalue:%.4f' %(tstat,pvalue))
print("*********************Three************************")
'''
3、计算输出变量两两之间的相关性，并为一些输入变量创建带有回归直线的散点图
'''
#计算所有变量的相关矩阵
print(wine.corr())
#从红葡萄酒和白葡萄酒的数据中取出一个“小”样本来进行绘图
def take_sample(data_frame,replace=False,n=200):
    return data_frame.loc[np.random.choice(data_frame.index,replace=replace,size=n)]
reds_sample = take_sample(wine.loc[wine['type']=='red',:])
white_sample = take_sample(wine.loc[wine['type']=='white',:])
wine_sample = pd.concat([reds_sample,white_sample])
wine['in_sample'] = np.where(wine.index.isin(wine_sample.index),1.,0.)
print(pd.crosstab(wine.in_sample,wine.type,margins=True))
#查看成对变量之家的关系
sns.set_style("dark")
g = sns.pairplot(wine_sample,kind='reg',plot_kws={"ci":False,"x_jitter":0.25,"y_jitter":0.25},
                 hue='type',diag_kind='hist',diag_kws={"bins":10,"alpha":1.0},palette=dict(red="red",white="white"),
                 markers=["o","s"],vars=['quality','alcohol','residual sugar'])
print(g)
plt.suptitle('Histogram and Scatter Plots of Quality,Alcohol,and Residual Sugar',fontsize=14,horizontalalignment='center',verticalalignment='top',
             x=0.5,y=0.999)
plt.show()
print("*********************Four************************")
'''
4、使用statsmodel包来进行线性回归（使用最小二乘法估计进行线性回归）
'''
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile acidity'
#使用公式和数据拟合一个普通最小二乘回归模型，并将结果赋给变量lm
lm = ols(my_formula, data=wine).fit()
#第二种方法，使用glm（广义线性模型）拟合同样的模型
#lm=glm(my_formula,data=wine,family=sm.families.Gaussian()).fit()
print(lm.summary())
print("\nQuantities you can extract from the result:\n%s" % dir(lm))
print("\nCoefficients:\n%s" % lm.params)
print("\nCoefficient Std Errors:\n%s" % lm.bse)
print("\nAdj. R-squared:\n%.2f" % lm.rsquared_adj)
print("\nF-statistic: %.1f  P-value: %.2f" % (lm.fvalue, lm.f_pvalue))
print("\nNumber of obs: %d  Number of fitted values: %s" % (lm.nobs, len(lm.fittedvalues)))