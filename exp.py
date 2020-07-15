# -*- coding:utf8 -*-
from gmpy2 import  invert,iroot,is_prime
from libnum import n2s,s2n
import time
n=int(open('C:\\Users\\jcbx\\Desktop\\N.txt','r').read())
c=int(open('C:\\Users\\jcbx\\Desktop\\C.txt','r').read())
print'start to calculate ...'
start=time.time()
e=0x10001
p=iroot(n+1,2)[0]-1
f=open('C:\\Users\\jcbx\\Desktop\\p.txt','w')
f.write(str(p))
# print n2s(m1)
# end=time.time() 
# print'Finish in {} seconds'.format(end-start)   

# m='Nep{e540b1fd7d4459619eecd244c12ae5c4}'
# c=pow(s2n(m),e,n)
# f.write(str(c))
# p=iroot(n+1,2)[0]-1
# q=p+2
# d=invert(e,(p-1)*(q-1))
# m1=pow(c%p,d%(p-1),p)
# print n2s(m1)

