# -*- coding:utf8 -*-
from itertools import *
import libnum

alphabet=list(range(256))


LETTER_FREQUENCY = {
    'e': 0.12702,
    't': 0.09056,
    'a': 0.08167,
    'o': 0.07507,
    'i': 0.06966,
    'n': 0.06749,
    's': 0.06327,
    'h': 0.06094,
    'r': 0.05987,
    'd': 0.04253,
    'l': 0.04025,
    'u': 0.02758,
    'w': 0.02560,
    'm': 0.02406,
    'f': 0.02228,
    'c': 0.02202,
    'g': 0.02015,
    'y': 0.01994,
    'p': 0.01929,
    'b': 0.01492,
    'k': 0.01292,
    'v': 0.00978,
    'j': 0.00153,
    'x': 0.00150,
    'q': 0.00095,
    'z': 0.00077,
    ' ': 0.2####################### very important   
    }


def desalt(cipher,salt):
    '''
    recover cipher before salt
    '''
    cp=[]
    salt=cycle(salt)
    for i,m in enumerate(cipher):
        if i % 2==0 and cipher[i+1]:
            t='0x'+cipher[i]+cipher[i+1]
            t=int(t,16)^ord(next(salt))
            cp.append(t)
    return cp

def IndCo(s):
    '''
    Index of Coincidence
    
    :param str s: The Substring.
    :return: The index of coincidence of the substring
    :rtype: float
    '''
    N=len(s)   
    frequency=[s.count(c) for c in alphabet]
    return sum(i**2-i for i in frequency)/float(N**2-N)

def CalKeyLength(s):
    '''
    Calculate the probable key lengths 
    :param ste s:The string to be analysed
    :return : All the probable key lengths
    :rtype :list
    '''
    res=[]
    for kl in range(8,50):
        subs=[s[i::kl] for i in range(kl)]#s[i::kl]��ָ�ӵ�i����ʼÿ��klȡһ�� ��subs��һ������
        #print sum(IndCo(si) for si in subs)/float(kl)
        if sum(IndCo(si) for si in subs)/float(kl) > 0.06:
            
            if all(map(lambda x: kl % x ,res)):# shaixuandiao na xie beishu 
                res.append(kl)
    return res

def score(s):
    score=0
    for i in s:
        if i in LETTER_FREQUENCY:
            score+=LETTER_FREQUENCY[i]
    return score
            
def RecoverKey(subs):
    keyword=''
    for s in subs:
        scores=[]
        for xor in alphabet:
            xored=''.join(chr(xor^x) for x in s)
            scores.append((xor,score(xored)))
        keyword+=chr(max(scores,key=lambda x:x[1])[0])
    return keyword
        
            
def main():

    
    op='49380d773440222d1b421b3060380c3f403c3844791b202651306721135b6229294a3c3222357e766b2f15561b35305e3c3b670e49382c295c6c170553577d3a2b791470406318315d753f03637f2b614a4f2e1c4f21027e227a4122757b446037786a7b0e37635024246d60136f7802543e4d36265c3e035a725c6322700d626b345d1d6464283a016f35714d434124281b607d315f66212d671428026a4f4f79657e34153f3467097e4e135f187a21767f02125b375563517a3742597b6c394e78742c4a725069606576777c314429264f6e330d7530453f22537f5e3034560d22146831456b1b72725f30676d0d5c71617d48753e26667e2f7a334c731c22630a242c7140457a42324629064441036c7e646208630e745531436b7c51743a36674c4f352a5575407b767a5c747176016c0676386e403a2b42356a727a04662b4446375f36265f3f124b724c6e346544706277641025063420016629225b43432428036f29341a2338627c47650b264c477c653a67043e6766152a485c7f33617264780656537e5468143f305f4537722352303c3d4379043d69797e6f3922527b24536e310d653d4c33696c635474637d0326516f745e610d773340306621105a7361654e3e392970687c2e335f3015677d4b3a724a4659767c2f5b7c16055a126820306c14315d6b59224a27311f747f336f4d5974321a22507b22705a226c6d446a37375761423a2b5c29247163046d7e47032244377508300751727126326f117f7a38670c2b23203d4f27046a5c5e1532601126292f577776606f0c6d0126474b2a73737a41316362146e581d7c1228717664091c'
    salt="WeAreDe1taTeam"
    cipher=[]
    ci=op.decode('hex')#strings to bytes
    si=cycle(salt) 
           
    for c in ci:       
        cipher.append((ord(c)^ord(next(si))))#recover str before salt
        
    kl=CalKeyLength(cipher)    
    print cipher
    kl=30#according to the previous step
       
    subs=[cipher[i::kl] for i in range(kl)]
       
    keyword=RecoverKey(subs)
    print keyword
       
    ki=cycle(keyword)
       
    plain=''.join(chr(s^ord(next(ki))) for s in cipher)#recover the plain
    print plain






#       alexctf-2017 cr2-many-time-secrets
#       op='0529242a631234122d2b36697f13272c207f2021283a6b0c79082f28202a302029142c653f3c7f2a2636273e3f2d653e25217908322921780c3a235b3c2c3f207f372e21733a3a2b37263b3130122f6c363b2b312b1e64651b6537222e37377f2020242b6b2c2d5d283f652c2b31661426292b653a292c372a2f20212a316b283c0929232178373c270f682c216532263b2d3632353c2c3c2a293504613c37373531285b3c2a72273a67212a277f373a243c20203d5d243a202a633d205b3c2d3765342236653a2c7423202f3f652a182239373d6f740a1e3c651f207f2c212a247f3d2e65262430791c263e203d63232f0f20653f207f332065262c31683137223679182f2f372133202f142665212637222220733e383f2426386b'
#       cipher=op.decode('hex')#strings to bytes
#       kl=26
#       subs=[cipher[i::kl] for i in range(kl)]
#       keyword=RecoverKey(subs)
#       print keyword
#       ki=cycle(keyword)
#       plain=''.join(chr(ord(s)^ord(next(ki))) for s in cipher)#recover the plain
#       print plain      
#       ke=list(keyword)
#       ke[10]='R'
#       ke[21]='_'
#       keyword=''.join(ke)
#       print keyword

      
if __name__=='__main__':
    main()        
            
     