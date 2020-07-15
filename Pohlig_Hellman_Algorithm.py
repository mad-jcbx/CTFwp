#coding=utf-8
import hashlib
import gmpy2
import libnum
import math
import sympy


def BSGS(y,z,p):
    '''
    y^x=z mod p
    '''
    m=int(math.ceil(gmpy2.iroot(p,2)[0]))
    dict={}
    for b in range(m):
        x=z*pow(y,b,p)%p
        dict[x]=b
    for a in range(m):
        if(pow(y,a*m,p) in dict.keys()):
            b=dict[pow(y,a*m,p)]
            break
    return (a*m-pow(y,a*m,p))


def Prime_power_Pohlig_Hellman(g,h,n,p,e):
    '''
    phi(n)=p^e
    g^(p^e)=1 mod n
    g^x=h mod n
    '''
    for a in range(e):
        if(pow(g,2**a,n)==1):
            break
    x_k=0
    e=a
    gm=pow(g,pow(p,e-1,n),n)
    print gm
    if(pow(g,p**e,n)!=1):
        print 'error'
    for k in range(e):
        _x=pow(p,e,n)-x_k
        if(pow(g,x_k,n)*pow(g,_x,n)%n !=1 ):
            print 'error'
        h_k=pow(pow(g,_x,n)*h,pow(p,e-1-k,n),n)
        for d_k in range(p):
            if(pow(gm,d_k,n)==h_k):
                print k,d_k
                break

        x_k=x_k+d_k*pow(p,k,n)
        
    return x_k  

if __name__ =='__main__':
    n=2**512
    m = 391190709124527428959489662565274039318305952172936859403855079581402770986890308469084735451207885386318986881041563704825943945069343345307381099559075
    c = 6665851394203214245856789450723658632520816791621796775909766895233000234023642878786025644953797995373211308485605397024123180085924117610802485972584499
    print libnum.n2s(Prime_power_Pohlig_Hellman(m, c, 2**512, 2, 511) )   


    