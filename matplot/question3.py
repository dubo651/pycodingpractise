# Question
"""
scores.xlsx部分内容如下：
编写一个能绘制学号-实验操作成绩折线图的小程序。
要求如下：
1）设置画布分辨率为200；
2）设置x轴刻度文本为学号，文本旋转90度；
提示：代码为plt.xticks(x,df['学号'],rotation=90) 
其中，rotation可以设置x轴刻度旋转90度。
3）设置y轴刻度范围为[0,100]；
提示：命令语句plt.ylim(最小值,最大值)
4）设置图标题为“实验操作成绩折线图”。
"""

# Answer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'
df = pd.read_excel('学号实验操作折线图/scores.xls', dtype={'学号':str})
# 绘制学号-实验操作折线图，分辨率200,x轴刻度值为学号
# ##补充代码开始
x = range(len(df['学号']))
plt.figure(dpi=200)
plt.plot(df['实验操作'])
plt.xticks(x, df['学号'], rotation=90)
plt.ylim(0, 100)
plt.title('实验操作成绩折线图')
# ##补充代码结束
plt.savefig('学号实验操作折线图/学号实验操作折线图.png')
plt.show()
