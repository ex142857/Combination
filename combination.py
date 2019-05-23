# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 15:41:16 2017

@author: jzj
"""

import pandas as pd
import itertools

x=pd.read_csv("receipts.csv")
list1=list(x['receipt'])
list2=[]
list3=[]
goal=x.values[0,1]

tlist=list(x['receipt'])
tlist.sort()
tlist.reverse()
ti=len(tlist)
ts=sum(tlist)
while (ts>=goal):
    tlist.pop()
    ti=ti-1
    ts=sum(tlist)

for i in range(ti+1,len(list1)+1):
    iter=itertools.combinations(list1,i)
    list2+=list(iter)

for i in range(0,len(list2)):
    s=sum(list2[i])
    list3.append(s)
    
df2=pd.DataFrame(list2)
df3=pd.DataFrame(list3)
df3.columns=['sum']
df=pd.concat([df2, df3], axis=1)
fdf=df[df['sum']>=goal]
sdf=fdf.sort_values('sum')

writer = pd.ExcelWriter('combination.xlsx')
sdf.to_excel(writer,'Sheet1')
writer.save()
