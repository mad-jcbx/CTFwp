from numpy import array
from string import alphabet


P1 = "RC4IsInteresting"
P2 = "ThisIsAEasyGame"


cipher1=hex(12078640933356268898100798377710191641).lstrip('0x').rstrip('L')
cipher2=hex(79124196547094980420644350061749775).lstrip('0x').rstrip('L')
cipher1='0'+cipher1
cipher2='0'+cipher2
c1=[]
c2=[]
for i in range(len(cipher1)/2):
    c1.append(int(cipher1[i*2]+cipher1[i*2+1],16))

for i in range(len(cipher2)/2):
    c2.append(int(cipher2[i*2]+cipher2[i*2+1],16))

rc41=[]
for i in range(len(P1)):
    rc41.append(ord(P1[i])^c1[i])
print rc41

rc42=[]
for i in range(len(P2)):
    rc42.append(ord(P2[i])^c2[i])
print rc42



class RC4():
    def __init__(self, Key):
        self.S = [i for i in range(256)]
        self.K = [ord(Key[i % len(Key)])*2 for i in range(256)]
        self.I, self.J = 0, 0
        self.KSA()

    def KSA(self):
        for i in range(256):
            j = (i+self.K[i]+self.S[i]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]

    def next(self):
        self.I = (self.I+1) % 256
        self.J = (self.J+self.S[self.I]) % 256
        self.S[self.J], self.S[self.I] = self.S[self.I], self.S[self.J]
        tmp = (self.S[self.J] + self.S[self.I]) % 256
        return self.S[tmp]
    
    
for a in alphabet


# ciphertext = 0
# for i in plain:
#     ciphertext = (ciphertext << 8)+ord(i) ^ self.rc4.next()

# ciphertext1 = 12078640933356268898100798377710191641
# ciphertext2 = 79124196547094980420644350061749775
