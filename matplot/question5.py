# Question
"""
本关任务：scores.xlsx部分内容如下：
编写一个能绘制班级1学生报告成绩条形图的小程序。
要求如下：
1）设置x值为df1长度对应序列[0,len(df1))
2）条形图xlabel为'学号'，ylabel为'成绩'
3）y轴刻度范围为[60,100]
4）图标题为'实验报告成绩图'
5）x轴刻度标签为班级1学生学号，旋转90度
6）图形分辨率200
"""

# Template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'
df = pd.read_excel('学号实验操作折线图/scores.xls',dtype={'学号':str})
# 绘制学生不同性别人数饼图，分辨率200
# ##补充代码开始
# 请为以下变量赋值
df1 =     #筛选出班级1所有学生行
x =         #设置为df1长度对应序列[0,len(df1))
height =    #设置条形的高度
dpi =       #设置分辨率200
title =     # 设置图形标题
xlabel =    #设置x轴标签
ylabel =    #设置为y轴标签
ymin =      #设置为y轴最小值
ymax =      #设置为y轴最大值
xticklabels =       #设置x刻度标签为班级1学生的学号
# ##补充代码结束
#请勿修改以下给定代码
plt.figure(dpi=dpi)      # 创建画布
plt.bar(x,height=height)  #绘制条形图
plt.title(title)   #添加标题
plt.xlabel(xlabel)  #添加x轴标签
plt.ylabel(ylabel)  #添加y轴标签
plt.ylim(ymin,ymax)  #设置y轴范围
plt.xticks(x,labels=xticklabels,rotation=90)
for a,b in zip(x,height):
    plt.text(a,b+0.3,'%.1f'%b,ha='center',va='bottom',fontsize=10)
plt.savefig('绘制实验报告条形图/实验报告条形图.png')
plt.show()

# Answer

df1 = df[df['班级名称'] == '班级1']
x = range(len(df1))
height = df1['实验报告'].tolist()
dpi = 200
title = '实验报告成绩图'
xlabel = '学号'
ylabel = '成绩'
ymin = 60
ymax = 100
xticklabels = df1['学号'].str[-6:].tolist()
