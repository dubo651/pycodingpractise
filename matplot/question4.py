# Question
"""
本关任务：scores.xlsx部分内容如下：
编写一个能绘制学生性别比例饼图的小程序。
要求如下：
1）对学生按照性别分组，统计各组内学生人数（即不同性别学生人数）；
2）设置画布分辨率为200；
3）绘制饼图，设置饼块标签文本为性别，图上显示不同性别百分比，保留一位小数；
4）设置图标题为"学生性别比例图"。
"""

# Answer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'
df = pd.read_excel('学号实验操作折线图/scores.xls', dtype={'学号':str})
# 绘制学生不同性别人数饼图，分辨率200
# ##补充代码开始
gender_counts = df.groupby('性别')['姓名'].count()

x = gender_counts.values.astype(float)
explode = [0] * len(gender_counts)
labels = gender_counts.index.tolist()
autopct = '%1.1f%%'
dpi = 200
title = '学生性别比例图'

# ##补充代码结束
plt.figure(dpi=dpi)
plt.pie(x, explode=explode, labels=labels, autopct=autopct)
plt.title(title)
plt.savefig('不同性别人数饼图/不同性别人数饼图.png')
plt.show()
```
