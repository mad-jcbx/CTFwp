# -*- coding:utf8 -*-
from gmpy2 import  invert,iroot,is_prime
from libnum import n2s,s2n
p=1679081223*pow(2,151618)-1
q=p+2
n=p*q
e=0x10001
m='flag{ca23d66d214bb93865679e86c893b7f8}'
print s2n(m)
c=pow(s2n(m),e,n)
f=open('C:\\Users\\jcbx\\Desktop\\cd.txt','w')
f.write(str(c))
