# -*- coding:utf8 -*-
#!/usr/bin/env python3
import libnum
import gmpy2
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
#import base64
from base64 import b64encode, b64decode
from crypto11 import flag
e=9850747023606211927
n=62078208638445817213739226854534031566665495569130972218813975279479576033261
p=184333227921154992916659782580114145999
q=336771668019607304680919844592337860739
mes="DWsGDe5mZXvs8l4kHjjteTLbV4rJ9JHwpUrZaQ/eqPT2YYiHwalRHZeobzcKRbBvcvqf1NYwJCuFwpDOnWK73bnQO06HaHdsSnRCqCy7slRnhs4QSIWkpeA3RlzSrDb/oNbuT8t/+HhlZbooWiCywnTsZWGjWwFvaGCvhEkZCLR17OB/7ZxXYhHaUCcyGmLGjpYEZGqGKU80Lu6VGenRRxmg4qsVI6T/GgXQjSZT43mIXCD+5g7zVUIfFAMQKYmwcYNWxOJZm7P9EbYQUTYNDU96hIgxrVCaMV7c1m5oLYdm99OkfyOk/lQ67KZLjSJIOSCmaJ3bHpuqDXdHPuxv9daB+31qu9eWQl2WuyuzM9U0Cd+oR+xMJcdGvLk/8wm+CPhkwnmMSVkYb7qXvaFZcap8/F5ZbzFAHLl+YKFsisRIq8iLQc1lttW7/E3dt4ds+ixfPakErgVUzKaziSDG1Ja/byqV9VdmqR0TCAtcIfmVZHu+doO1HnOJlmIb6IDwuBSwba825/E4sMM24RK/PscuXaAQGAkyKI+apX7PUObFE6XA7KMSDleikIQ7HYFsGJISGzbP0mX6iFn8qoUI82p98y2grsNBGKm3uBb3Zump8eqgJh5MMdiPCRir5uRPZpT6weepqr3i7uPTLy91QpXeG7b2OowRs6MmEB8vxyLkhIJvJrNTehXmb/2EXJwXQBEqiDAJ0+0QE0PUsegHqcYIoMNtHFt4UPX7Dm2p+Mi9a+fnXzC9GMUwqcL6JXG8W6V9yWSUBoG2mIhCX/dM2Cnrm3wprccV+Hi4gdnEfRKuDjuVBAJ0kBQrGjwK1JgoWbIItmwxGKu70olIwQN7LspUCiJH3Bkalo9crFTDGFJr7qBdMz2+7FBb7hYT9mLSxAo1UoZYtraQJoxNJQs81rG8IPq27upPj6xenTFYHhSRnJwEFAOvam2+rXTnyQO2DME="
m=int(b64decode(mes).encode('hex'),16)
while True:       
    n = p * q
    try:       
        phi = (p - 1)*(q - 1)
        d=gmpy2.invert(e,phi)
        pubkey = RSA.construct((int(n), int(e),int(d)))
        key = PKCS1_v1_5.new(pubkey)
        flag=key.decrypt(m,'ERROR')
        print flag
        return flag
    except:
        p = gmpy2.next_prime(p**2 + q**2)
        q = gmpy2.next_prime(2*p*q)
        e = gmpy2.next_prime(e**2)

'''
曹，就是忘了字符串要先进行十六进制编码再进行RSA解密   
'''
    
    
    