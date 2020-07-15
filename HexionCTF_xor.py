# enc.py
# from random import choice, randint
# from string import ascii_letters
# from itertools import cycle
# 
# key = ''.join([choice(ascii_letters) for i in range(randint(8, 16))])
# 
# with open("flag.txt", "r") as file:
#     flag = file.read()
# 
# key_gen = cycle(key)
# data = []
# for i in range(len(flag)):
#     data.append(chr(ord(flag[i]) ^ ord(next(key_gen))))
# 
# with open("flag.enc", "w+") as file:
#     file.write(''.join(data))

#-----------------------------------------------------------------------
# -*- coding:utf8 -*-
from itertools import *
import libnum
from string import ascii_letters




alphabet=[ord(i) for i in ascii_letters]

cho=alphabet+['0','1','2','3','4','5','6','7','8','9','_']

print cho

print alphabet
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
#    ' ': 0.2####################### very important   
    }


def score(s):
    score=0
    for i in s:
        if i in LETTER_FREQUENCY:
            score+=LETTER_FREQUENCY[i]
    return score
            
def RecoverKey(subs,kl):
    keyword='JtmZzCJ'
    for s in range(len(subs)-8):
        for xor in alphabet:
            xored=''
            for x in subs[s+7]:             
                if chr(xor^x) not in cho:
                    break
                else:
                    keyword+=chr(xor)
    

            
                       
#             xored=''.join(chr(xor^x) for x in s)
#         keyword+=chr(max(scores,key=lambda x:x[1])[0])

    return keyword
        
            
if __name__=='__main__':
    cipher=[ord(i) for i in open('src\\xor_flag.enc','r').read()]
    print cipher
    for kl in range(10,11):
        subs=[cipher[i::kl] for i in range(kl)]
        keyword=RecoverKey(subs,kl)
        print keyword
        ki=cycle(keyword)
        plain=''.join(chr(s^ord(next(ki))) for s in cipher)
        print plain
        
        


