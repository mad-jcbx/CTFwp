# -*- coding:utf8 -*-
from gmpy2 import  invert,iroot,is_prime
from libnum import n2s,s2n
n=int(open('C:\\Users\\jcbx\\Desktop\\N.txt','r').read())
c=int(open('C:\\Users\\jcbx\\Desktop\\C1.txt','r').read())
e=0x10001
p=iroot(n+1,2)[0]-1
q=p+2
d=invert(e,(p-1)*(q-1))
m1=pow(c%p,d%(p-1),p)
print n2s(m1)