import itertools 
import math
import numpy as np

def digest(arr,M):
    arr.sort()
    for i in range(len(arr)):
        Sum=sum(arr)
    if Sum==M and arr not in x:
        x.append(arr)

def helper(x,y):
    temp=[]
    for i in x:
        temp.append(i)
    for j in y:
        temp.append(j)
    temp.sort()
    return temp

def mapping(x,l2):
    temp2=[]
    for i in range(int(len(x)/2)):
        for j in range(i+1,len(x)):
            temp=helper(x[i],x[j])
            if temp == l2 :
                temp2.extend([[x[i],x[j]]])
    return temp2

def possible(enz):
    temp=[]
    for j in range(1,len(enz)):
        for i in itertools.combinations(enz,j):
            temp.append(list(i))
    return temp


enz=[1,2,3,4,5,3]
enz.sort()
x=[]
M=int(sum(enz)/2)
possibleLength=possible(enz)
#print(possibleLength)
for i in possibleLength :
    digest(i,M)
    
Map=mapping(x,enz)
for i in Map:
    print(i)

