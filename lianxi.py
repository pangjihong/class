with open('report.txt',encoding='utf-8') as f:
    data=f.readlines()
    #print(data)

#添加名次，总分，平均分选项
score=[]
for data1 in data:
   # print(data1)
   score.append(data1.split())
#print(score)
score[0].insert(0,'名次')
score[0].append('总分')
score[0].append('平均分')
#print(score)
#求成绩总数，平均数
for a in score[1:]:
    data_sum = 0
    data_ave = 0
    for b in a[1:]:
        data_sum+=int(b)
    data_ave=round(data_sum/9,1)
    a.append(str(data_sum))
    a.append(str(data_ave))
   # print(a)
#print(score)

#对平均分进行排序
score.sort(key=lambda a:a[-1],reverse=True)
#print(score)

#汇总每一科目的平均分和总平均分
subject=[]
for i in range(1,12):
    subject_sum=0
    subject_ave =0
    for k in score[1:]:
        subject_sum+=float(k[i])
    subject_ave=round(subject_sum/len(score)-1,1)
    subject.append(str(subject_ave))
subject.insert(0,'平均')
#print(subject)
score.insert(1,subject)
#print(score)

#添加名次,替换60分以下为不合格
num=-1
for i in score[1:]:
    num+=1
    i.insert(0,str(num))
#print(score)
    for m in range(2,10):
        if float(i[m])<60:
            i[m]=str('不及格')
#print(score)

#讲处理后的成绩另存为新文件
result=[]
for h in score:
    #print(h)
    line=' '.join(h)+'\n'
    result.append(line)

with open('result.txt','w',encoding='utf-8') as f1:
    data=f1.writelines(result)














































