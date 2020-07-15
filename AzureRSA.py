# -*- coding:utf8 -*-
n1=0xcfc59d54b4b2e9ab1b5d90920ae88f430d39fee60d18dddbc623d15aae645e4e50db1c07a02d472b2eebb075a547618e1154a15b1657fbf66ed7e714d23ac70bdfba4c809bbb1e27687163cb09258a07ab2533568192e29a3b8e31a5de886050b28b3ed58e81952487714dd7ae012708db30eaf007620cdeb34f150836a4b723L
e1=0xfae3aL
c1=0x81523a330fb15125b6184e4461dadac7601340960840c5213b67a788c84aecfcdc3caf0bf3e27e4c95bb3c154db7055376981972b1565c22c100c47f3fa1dd2994e56090067b4e66f1c3905f9f780145cdf8d0fea88a45bae5113da37c8879c9cdb8ee9a55892bac3bae11fbbabcba0626163d0e2e12c04d99f4eeba5071cbeaL
n2=0xd45304b186dc82e40bd387afc831c32a4c7ba514a64ae051b62f483f27951065a6a04a030d285bdc1cb457b24c2f8701f574094d46d8de37b5a6d55356d1d368b89e16fa71b6603bd037c7f329a3096ce903937bb0c4f112a678c88fd5d84016f745b8281aea8fd5bcc28b68c293e4ef4a62a62e478a8b6cd46f3da73fa34c63L
e2=0x1f9eaeL
c2=0x4d7ceaadf5e662ab2e0149a8d18a4777b4cd4a7712ab825cf913206c325e6abb88954ebc37b2bda19aed16c5938ac43f43966e96a86913129e38c853ecd4ebc89e806f823ffb802e3ddef0ac6c5ba078d3983393a91cd7a1b59660d47d2045c03ff529c341f3ed994235a68c57f8195f75d61fc8cac37e936d9a6b75c4bd2347L
from libnum import *
import gmpy2

p = gcd(n1,n2)
q1 = n1/p
q2 = n2/p

a1=e1/14
a2=e2/14
#e = a*b  b = 14
bd1 = gmpy2.invert(a1,(p-1)*(q1-1)) # a*b*d = 1 mod (p-1)(q-1)    c^bd1 = m^14 mod n1
bd2 = gmpy2.invert(a2,(p-1)*(q2-1))# c^bd2 = m^14 mod n2

res1 = pow(c1,bd1,p)#或者res1 = pow(c2,bd2,p)
res2 = pow(c1,bd1,q1)
res3 = pow(c2,bd2,q2)
print res1
print res2
print res3

m = solve_crt([res1,res2,res3],[p,q1,q2]) # m^14

n = q1*q2
m = m%n
f = (q1-1)*(q2-1)
d = gmpy2.invert(7,f)
m2 = pow(m,d,n)
m = gmpy2.iroot(m2, 2)[0]
print n2s(m)
    