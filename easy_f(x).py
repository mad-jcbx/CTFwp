# -*- coding:utf8 -*-
import gmpy2
import os
import time
import random
data=[]
file=open('C:\\Users\\jcbx\\Desktop\\f(x).txt','r')
for line in file.readlines():    
    curLine=line.lstrip("f(").split(")=")    
    floatLine=map(int,curLine)
    data.append(floatLine) 
print data[30]
print data[1][1]

