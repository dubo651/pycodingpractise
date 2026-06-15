# 查询员工销售信息
# 请勿修改已有代码
import pandas as pd

df=pd.read_csv('src/销售表.csv',names=["员工编号","姓名","销售团队","一月份","二月份","三月份"])
## 补充代码开始
df.columns=['员工编号','姓名','销售团队','一月份','二月份','三月份']
df['第一季度']=df['一月份']+df['二月份']+df['三月份']
df.to_excel('step5/销售表zj.xlsx',index=False)

## 补充代码结束

bh = input()  #输入要查询的员工编号
df = pd.read_excel('step5/销售表zj.xlsx')
je = df.loc[df['员工编号']==bh,['第一季度']]
print(je)
