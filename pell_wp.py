# -*- coding:utf8 -*-
import gmpy2
import os,random,sys,string
import libnum
from Crypto.Util.number import *
from hashlib import sha256,sha512


# while 1:
#     proof = ''.join([random.choice(string.ascii_letters+string.digits) for _ in xrange(4)])
#     if sha256(proof+'fsWtxSRIZNb52hxz').hexdigest() == '7eb7ed7bac125f08b9ec09a4b9744258f2d88aee8f921a6db6fd3ad4d2aeec47':
#         print proof
#         break
      
a = 14
b = 1
c=[]
y=2
       
while(gmpy2.iroot(a*y**2+b,2)[1]!=True):
    y+=1
print y   
c.append((gmpy2.iroot(a*y**2+b,2)[0],y))
print c
a = 14
b = 1
c=[]
y=2

x1=15
y1=4
D=a
for i in range(15):
    x=x1**2+D*y1**2
    y=2*x1*y1
    print x
    print y
    x1=x
    y1=y
     
              
      