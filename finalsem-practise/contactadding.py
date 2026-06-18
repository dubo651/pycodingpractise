# 增加联系人及电话号码
keys = [] 
dic = {}
fname = '/data/workspace/myshixun/step7/通信簿.txt'
fr = open(fname,'r')
for line in fr:
    line = line.replace("\n",'')
    v = line.split('\t')
    dic[v[0]] = v[1]
    keys.append(v[0])
fr.close()
jx='y'
while(jx=='y'):
    key = input()   #"请输入姓名："
    tele = input()  #"请输入电话："
    ## Begin  ##
    if key in dic:
        print("联系人已存在")
    elif len(tele) == 11 and tele.isdigit():
        fw = open(fname, 'a')
        fw.write(key + '\t' + tele + '\n')
        fw.close()
        dic[key] = tele
        keys.append(key)
        print("增加成功")
    else:
        print("电话号码必须是11位")
    ## End ##
    print("是否继续添加联系人?")
    jx=input()   #"是否继续"
print('程序结束')
