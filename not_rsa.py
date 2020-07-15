# -*- coding:utf8 -*-
import cmath
import gmpy2
import random
from libnum import  *
from libnum import  *
p = 80006336965345725157774618059504992841841040207998249416678435780577798937819
q = 80006336965345725157774618059504992841841040207998249416678435780577798937447
c = 29088911054711509252215615231015162998042579425917914434962376243477176757448053722602422672251758332052330100944900171067962180230120924963561223495629695702541446456981441239486190458125750543542379899722558637306740763104274377031599875275807723323394379557227060332005571272240560453811389162371812183549

n=p*q
g=n+1
_q=gmpy2.invert(q,p-1)
_p=gmpy2.invert(p,q-1)
r=solve_crt([pow(c%n,_q,p),pow(c%n,_p,q)], [p,q])
print r
_n=gmpy2.invert(n,(p-1)*(q-1))
print pow(c%n,_n,n)

_rn=gmpy2.invert(pow(r,n,n*n),n*n)
a=(_rn*c)%(n*n)-1
m=(a/n)%n
print n2s(m)
#How to calculate (n+1)^m = k mod n*n we need m
#If we know m^-1
#How to calc K^(m^-1) = (n+1) mod n*n


    
    