from hashlib import *
from libnum import*
# tar = "000000000000000000000"
S = ""
for h in range(32, 127):
    S += chr(h)
# 
# for h in S:
#     for i in S:
#         for j in S:
#             for k in S:
#                 x = sha256((h+i+j+k+'pS70GlerItmmoOWS').encode()).hexdigest()
#                 
#                 if x=="xxx":
#                     print(x)
#                     print(h+i+j+k)
#                     quit()
# print("DONE")
from hashlib import *
from libnum import*
S = ""
for h in range(32, 127):
    S += chr(h)
for h in S:
    for i in S:
        for j in S:
            for k in S:
                t=sha256(h+i+j+k+"513e0aeae0a81b0ec53fa47524f0a78d".decode('hex')).hexdigest()
                if(bin(int(t,16)).endswith("000000000000000000000")):
                     print(h+i+j+k)
                     print hex(s2n(h+i+j+k)).lstrip("0x")
                     quit()               