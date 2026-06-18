# Question
"""
本关任务：编写一个能绘制正弦曲线的小程序。
编程要求
根据提示，在右侧编辑器补充代码，计算x的值及对应的sin(x)，并输出对应的正弦曲线折线图。x的取值范围[0,10)，起始值0，步长0.5。绘制的图形保存在“绘制基本折线图/sinx.png”文件中，图形分辨率为800。
"""
# Template and answer
# 绘制基本折线图
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False  #显示负号
plt.figure()
##  补充代码开始
x = np.arange(0, 10, 0.5)
y = np.sin(x)
plt.plot(x, y)
plt.savefig('绘制基本折线图/sinx.png', dpi=800)
plt.show()
## 补充代价结束
