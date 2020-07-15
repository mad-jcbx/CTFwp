from libnum import *
from Crypto.Util.number import*
# from secret import flag

li=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
for i in li: 
    for j in li:
        for k in li:
            for l in li:
                seed=int((hex(state1)+i+j+k+l),16)
                if((seed*a+b)%m>>16==state2):
                    print seed
                    break
                
                
class LCG:
    def __init__(self):
        self.a = 3844066521
        self.b = 3316005024
        self.m = 2249804527
        self.seed =1066209821#1066229421#1066249021#1066268621#[,,,]
    def next(self):
        self.seed = (self.a*self.seed+self.b) % self.m
        return self.seed >> 16

    def output(self):
        print("a = {}\nb = {}\nm = {}".format(self.a, self.b, self.m))
        print("state2 = {}".format(self.next()))
#         print("state2 = {}".format(self.next()))


class DH:
    def __init__(self):
        self.lcg = LCG()
        self.lcg.output()
        self.g = 183096451267674849541594370111199688704
        self.m = 102752586316294557951738800745394456033378966059875498971396396583576430992701
        self.A, self.a = self.gen_AB()
        self.B, self.b = self.gen_AB()
        self.key = pow(self.A, self.b, self.m)

    def gen_AB(self):
        x = ''
        for _ in range(64):
            x += '1' if self.lcg.next() % 2 else '0'
        return pow(self.g, int(x, 2), self.m), int(x, 2)


DH = DH()
# flag = bytes_to_long(flag)
print("g = {}\nA = {}\nB = {}\nM = {}".format(DH.g, DH.A, DH.B, DH.m))
key=pow(DH.A,DH.b,DH.m)
Cipher = 13040004482819935755130996285494678592830702618071750116744173145400949521388647864913527703
print n2s(Cipher^key)
# print("Cipher = {}".format(flag ^ DH.key))


'''
a = 3844066521
b = 3316005024
m = 2249804527
state1 = 16269
state2 = 4249
g = 183096451267674849541594370111199688704
A = 102248652770540219619953045171664636108622486775480799200725530949685509093530
B = 74913924633988481450801262607456437193056607965094613549273335198280176291445
M = 102752586316294557951738800745394456033378966059875498971396396583576430992701
Cipher = 13040004482819935755130996285494678592830702618071750116744173145400949521388647864913527703
'''