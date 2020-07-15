# -*- coding:utf8 -*-
import gmpy2
n=0xc2636ae5c3d8e43ffb97ab09028f1aac6c0bf6cd3d70ebca281bffe97fbe30dd
p=319576316814478949870590164193048041239
q=275127860351348928173285174381581152299
d =0x1806799bd44ce649122b78b43060c786f8b77fb1593e0842da063ba0d8728bf1
e =2
c = int(open('flag.enc','rb').read().encode('hex'),16)

c1=pow(c,(p+1)/4,p)
c2=pow(c,(q+1)/4,q)
cp1=p-c1
cp2=q-c2
t1=gmpy2.invert(p,q)#p的模q逆元
t2=gmpy2.invert(q,p)#q的模p逆元

m1=(q*c1*t2+p*c2*t1)%n
m2=(q*c1*t2+p*cp2*t1)%n# or m2=n-m1
m3=(q*cp1*t2+p*c2*t1)%n
m4=(q*cp1*t2+p*cp2*t1)%n# or m4=n-m3

for i in(m1,m2,m3,m4):
    m = '%x' % i
    if len(m)%2==1:
        m='0'+m
    print(m.decode('hex'))    
    
