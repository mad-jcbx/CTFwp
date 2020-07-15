from string import ascii_lowercase as alphabet
from gmpy2 import gcd,invert
from itertools import *
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

def score(s):
    score=0
    for i in s:
        if i in LETTER_FREQUENCY:
            score+=LETTER_FREQUENCY[i]
    return score


def main():
    kl=3
    cipher=[23, 116, 1, 80, 75, 1, 37, 39, 44, 18, 39, 67, 23, 30, 44, 37, 10, 96, 46, 58, 124, 32, 110, 1, 74, 1, 39, 3, 39, 58, 60, 1, 96, 23, 58, 115, 117, 61]
    alist=[]
    for a in range(128):
        if(gcd(a,128)==1):
            alist.append(a)       

    subs=[cipher[i::kl] for i in range(kl)]
    a=57
    for xor in alphabet:
        if(chr(((cipher[2]-ord(xor))*invert(a,128))%128)=='a' ):
            print (xor)
                
                
    a=57
    keyword=['a','h','h']
    m=''
    k1=cycle(keyword)
    for i in cipher:
        m+=chr((i-ord(next(k1)))*invert(a,128)%128)
    print m

         
        
    
if __name__ =='__main__':
    main()