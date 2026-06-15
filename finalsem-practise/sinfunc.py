import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False  #显示负号
matplotlib.rcParams['font.family']='SimHei'  #显示汉字
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

def trqx():
    plt.figure(figsize=(8,5))   #创建绘图区域为8英寸宽5英寸高
    ###  1.补充代码 Begin  ###
    #确定所取点的x坐标值
    x=np.arange(0,4*np.pi,0.01)
    #得到sin(x)/2曲线上点的y坐标值
    y1=np.sin(x)/2
    #得到-sin(x)曲线上点的y坐标值
    y2=-np.sin(x)
    #绘制sin(x)/2曲线，红色虚线
    plt.plot(x,y1,'r--',label=r'$y=\sin(x)/2$')
       #绘制-sin(x)曲线,绿色加粗
    plt.plot(x,y2,'g-',label=r'$y=-\sin(x)$')
    ###  1.End  ###
    
    plt.xticks([0, np.pi/2, np.pi,np.pi*3/2,np.pi*2,np.pi*5/2,np.pi*3,np.pi*7/2, np.pi*4, ],
               [r'0', r'$\frac{1}{2}\pi$','$\pi$',r'$\frac{3}{2}\pi$',r'$2 \pi$',
                r'$\frac{5}{2} \pi$',r'$3\pi$',r'$\frac{7}{2}\pi$',r'$4 \pi$'])
    ###  2.补充代码 Begin  ###
    #设置x轴刻度范围为[0,4*np.pi]
    plt.xlim(0,4*np.pi)
    #设置y轴刻度范围为[-1,1]
    plt.ylim(-1,1)
    #设置标题为“三角函数曲线”
    plt.title('三角函数曲线')
    #设置横坐标标签为“横坐标”
    plt.xlabel('横坐标')
    #设置纵坐标标签为“纵坐标”
    plt.ylabel('纵坐标')
    
    
    ###  2.End  ###
    plt.savefig('image1/trqx.png')
    plt.show()

#主程序如下
trqx()
