# -*- coding:utf8 -*-
import gmpy2
from libnum import  *
import random
import math
from scipy.special import cbrt
import time

def onemod(e,q):
    p=random.randint(1,q-1)
    while(pow(p,(q-1)/e,q)==1):#(r,s)=1
         p=random.randint(1,q)
    return p

def AMM_rth(o,r,q):# r|(q-1)
    print'start to calculate primitive root...'
    start=time.time()
    assert((q-1)%r==0)
    p=onemod(r,q)
    print 'p:%d'%p

    t=0
    s=q-1
    while(s%r==0):
        s=s/r
        t+=1
    k=1    
    while((s*k+1)%r!=0):
        k+=1
    alp=(s*k+1)/r
    
    print 's:%d,t:%d r:%d alp:%d'%(s,t,r,alp)
    a=pow(p,r**(t-1)*s,q)
    b=pow(o,r*a-1,q)
    c=pow(p,s,q)
    h=1
    
    for i in range(1,t-1):
        d=pow(int(b),r**(t-1-i),q)
        print 'd:%d'%d
        if d==1:
            j=0
        else:
            j=(-math.log(d,a))%r
        b=(b*(c**(r*j)))%q
        h=(h*c**j)%q
        c=(c*r)%q
    result=(pow(o,alp,q)*h)
    end=time.time()
    
    print 'result:%d'%result
    print'Finish in {} seconds'.format(end-start)
    return result
#由于理解不到位，所以算法有问题   because of my fool, the algorithm have problem.//2020.4.3 finish

def ALL_ROOT(r,q):#最后数组会有重复
    print'start to calculate all primitve root...'
    start=time.time()
    rt=[]
    while(len(rt)<=2*r):       
        p=pow(random.randint(1,q-1),(q-1)/r,q)# 都一样onemod(r,q)
        rt.append(p)  
    end=time.time() 
    print'Finish in {} seconds'.format(end-start)   
    return rt
        
def ALL_Solution(m,q,rt,cq,e):
    print'start to calculate all root...'
    start=time.time()
    mp=[]
    for pr in rt:
        r=(pr*m)%q
        assert(pow(r,e,q)==cq)
        mp.append(r)
    end=time.time()
    print'Finish in {} seconds'.format(end-start)
    return mp
       
def calc(mp,mq,e,p,q):
    print'satrting crt... '
    i=1
    j=1
    start=time.time()
    t1=gmpy2.invert(q,p)
    t2=gmpy2.invert(p,q)
    for mp1 in mp: 
        if(j%1000==0):
            print j
        j+=1           
        for mq1 in mq:
            ans=(mp1*t1*q+mq1*t2*p)%(p*q)
            if check(ans):
                print'Finish in {} seconds'.format(time.time()-start)
                return 
                      
    return 
    
def check(m):
    try:
        a=n2s(m)
        if a.startswith('NCTF'):
            print a
            return True
        else:
            return False
    except:
        return False


def ALL_ROOT2(r,q):#use function set() and .add() ensure that the generated elements are not repeated
    print'start to find all primitive root...'
    start=time.time()
    li=set()
    while(len(li)<r):
        p=pow(random.randint(1,q-1),(q-1)/r,q)
        li.add(p)
    end=time.time()
    print'Finish in {} seconds'.format(end-start)
    return li
    
        
def  test(cp,e,p):
    print'start to calculate all primitve root...'
    start=time.time()
    (g,s,t)=gmpy2.gcdext(e,p)
    rt=pow(cp,s%p,p)
    print 'result:%d'%rt
    end=time.time() 
    print'Finish in {} seconds'.format(end-start)   
    return rt

if __name__=='__main__':
    c = 10562302690541901187975815594605242014385201583329309191736952454310803387032252007244962585846519762051885640856082157060593829013572592812958261432327975138581784360302599265408134332094134880789013207382277849503344042487389850373487656200657856862096900860792273206447552132458430989534820256156021128891296387414689693952047302604774923411425863612316726417214819110981605912408620996068520823370069362751149060142640529571400977787330956486849449005402750224992048562898004309319577192693315658275912449198365737965570035264841782399978307388920681068646219895287752359564029778568376881425070363592696751183359
    p = 199138677823743837339927520157607820029746574557746549094921488292877226509198315016018919385259781238148402833316033634968163276198999279327827901879426429664674358844084491830543271625147280950273934405879341438429171453002453838897458102128836690385604150324972907981960626767679153125735677417397078196059
    q = 112213695905472142415221444515326532320352429478341683352811183503269676555434601229013679319423878238944956830244386653674413411658696751173844443394608246716053086226910581400528167848306119179879115809778793093611381764939789057524575349501163689452810148280625226541609383166347879832134495444706697124741
    e = 0x1337
    cp=c%p
    cq=c%q
    
    
    mp=AMM_rth(cp,e,p)
    mq=AMM_rth(cq,e,q)
     
     
    rt1=ALL_ROOT2(e,p)
    rt2=ALL_ROOT2(e,q)
 
     
#     rt1=ALL_ROOT(e,p)
#     rt2=ALL_ROOT(e,q) 
           
    amp=ALL_Solution(mp,p,rt1,cp,e)
    amq=ALL_Solution(mq,q,rt2,cq,e)
        
    calc(amp, amq,e,p,q)
    
    
    
#     i1=133043033237947900331501573748238988276844558598707196266270361130476915500252594753135696450496348680137409211655110608440000560206185800679840810619025689783829158433712853891359973625940459905472355647218768144592509196298332000507993973890088045947197235777184735740067052612166444587145601447366057033636
#     i2=104285040343098512281111264956795310506222667776552033187921259683715123085781881343131194007657118808516855040448890402367677678214752753598867917253530749851176201769563523953764459214439878523379692059283383437503476585832881258150371570024665996981835551110347781858952143532822442922795428743076727053990
#   
#     if i1 in amp:
#         print'i1 ok'
#         print amp.index(i1)
#            
#     if i2 in amq:
#         print'i2 ok'
#         print amq.index(i2)
           
#     t1=gmpy2.invert(q,p)
#     t2=gmpy2.invert(p,q)   
#     ans=(i1*t1*q+i2*t2*p)%(p*q)
#     if check(ans):
#         print'Finish!'
#     #i2没有，也就是amq有问题//2020.4.3 22:31 question is randint(1,q-1)
#     all wrong. Because it's a huge randomness.So our amp and amq need  more elements.
        
    


            
    
    
    
    
            