import pandas as pd
from scipy.stats.stats import pearsonr
import numpy as np
#import datetime as dt
dataset = pd.read_csv('suspect_times.csv')
name=dataset.iloc[:,0].values
time=dataset.iloc[:,2].values

d=[]
m=[]
y=[]
hr=[]
mi=[]
c=[]
b=[]
for i in time:
    d.append(i[:2])
    m.append(i[3:5])
    y.append(i[7:12])
    hr.append(i[11:13])
    mi.append(i[14:16])


#[6,13,20,27,1,8,15,22,29])
#[4,6,11,13,18,20,25,27]
#remove 17 from hr    
for i in range(0,len(name)):
    if (m[i]=='11' and d[i]  not in ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','27','29']) or (m[i]=='12' and (d[i] not in ['04','06','11','13','18','20','25','27','28','29','30','31'])) and (hr[i] in ['15','16','17']) :
        c.append((name[i],time[i]))

#print(c)

for i in c:
    if i[1][-1]=='0':
        b.append(i)
print(b)        


