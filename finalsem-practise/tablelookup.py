# 查询员工销售信息
import pandas as pd

df=pd.read_csv('src/销售表.csv',names=["员工编号","姓名","销售团队","一月份","二月份","三月份"])
bh = input()  #输入要查询的员工编号

## 补充代码开始
emp=df[df['员工编号']==bh]
if emp.empty:
    print("查无此人")
else:
    row=emp.iloc[0]
    if row['一月份']<=80000:
        print("一月份销售额不到80000")
    else:
        print(emp)

## 补充代码结束
