#coding=utf-8
import hashlib
import gmpy2
import libnum



def pad_even(x):
    return ('', '0')[len(x)%2] + x

def e_3(n,e,c):
    '''
    Recover the m when e is 3
    :param int n:The N
    :param int e:The e
    :param int c:The ciphertext
    
    for example:
    n = 0x52d483c27cd806550fbe0e37a61af2e7cf5e0efb723dfc81174c918a27627779b21fa3c851e9e94188eaee3d5cd6f752406a43fbecb53e80836ff1e185d3ccd7782ea846c2e91a7b0808986666e0bdadbfb7bdd65670a589a4d2478e9adcafe97c6ee23614bcb2ecc23580f4d2e3cc1ecfec25c50da4bc754dde6c8bfd8d1fc16956c74d8e9196046a01dc9f3024e11461c294f29d7421140732fedacac97b8fe50999117d27943c953f18c4ff4f8c258d839764078d4b6ef6e8591e0ff5563b31a39e6374d0d41c8c46921c25e5904a817ef8e39e5c9b71225a83269693e0b7e3218fc5e5a1e8412ba16e588b3d6ac536dce39fcdfce81eec79979ea6872793L
    e = 3
    c = 0x10652cdfaa6b63f6d7bd1109da08181e500e5643f5b240a9024bfa84d5f2cac9310562978347bb232d63e7289283871efab83d84ff5a7b64a94a79d34cfbd4ef121723ba1f663e514f83f6f01492b4e13e1bb4296d96ea5a353d3bf2edd2f449c03c4a3e995237985a596908adc741f32365
    '''   
    for i in range(0,150000000):
        m=gmpy2.iroot(c+n*i,3)
        i=i+1
        print(i)
        if m[1] == True:
            print(m[0])
            break
    print libnum.n2s(m[0])

def Common_e_Attack(N,e1,e2,c1,c2):

    (t,x,y)=gmpy2.gcdext(e1,e2)
    print(t)
    print('x=%s,y=%s'%(x,y))
    c2_=gmpy2.invert(c2,N)
    m =pow(c1,x,N)*pow(c2_,-y,N)%N 

    m = pad_even('%x'%m)
    print(m.decode('hex'))

def Rabin(n,p,q,c):
    '''
    for example:
    n =0xc2636ae5c3d8e43ffb97ab09028f1aac6c0bf6cd3d70ebca281bffe97fbe30dd
    p=319576316814478949870590164193048041239
    q=275127860351348928173285174381581152299
    d =0x1806799bd44ce649122b78b43060c786f8b77fb1593e0842da063ba0d8728bf1
    e =2
    '''
    c1=pow(c,(p+1)/4,p)
    c2=pow(c,(q+1)/4,q)
    cp1=p-c1
    cp2=q-c2
    t1=gmpy2.invert(p,q)#p的模q逆元
    t2=gmpy2.invert(q,p)#q的模p逆元

    m1=(q*c1*t2+p*c2*t1)%n
    m2=(q*c1*t2+p*cp2*t1)%n# or m2=n-m1
    m3=(q*cp1*t2+p*c2*t1)%n
    m4=(q*cp1*t2+p*cp2*t1)%n# or m4=n-m3

    for i in(m1,m2,m3,m4):
        m = '%x' % i
        if len(m)%2==1:
            m='0'+m
            print(m.decode('hex'))    
    


def main():
    n=0xa1d4d377001f1b8d5b2740514ce699b49dc8a02f12df9a960e80e2a6ee13b7a97d9f508721e3dd7a6842c24ab25ab87d1132358de7c6c4cee3fb3ec9b7fd873626bd0251d16912de1f0f1a2bba52b082339113ad1a262121db31db9ee1bf9f26023182acce8f84612bfeb075803cf610f27b7b16147f7d29cc3fd463df7ea31ca860d59aae5506479c76206603de54044e7b778e21082c4c4da795d39dc2b9c0589e577a773133c89fa8e3a4bd047b8e7d6da0d9a0d8a3c1a3607ce983deb350e1c649725cccb0e9d756fc3107dd4352aa18c45a65bab7772a4c5aef7020a1e67e6085cc125d9fc042d96489a08d885f448ece8f7f254067dfff0c4e72a63557
    e1=0xf4c1158f
    c1=0x2f6546062ff19fe6a3155d76ef90410a3cbc07fef5dff8d3d5964174dfcaf9daa003967a29c516657044e87c1cbbf2dba2e158452ca8b7adba5e635915d2925ac4f76312feb3b0c85c3b8722c0e4aedeaec2f2037cc5f676f99b7260c3f83ffbaba86cda0f6a9cd4c70b37296e8f36c3ceaae15b5bf0b290119592ff03427b80055f08c394e5aa6c45bd634c80c59a9f70a92dc70eebec15d4a5e256bf78775e0d3d14f3a0103d9ad8ea6257a0384091f14da59e52581ba2e8ad3adb9747435e9283e8064de21ac41ab2c7b161a3c072b7841d4a594a8b348a923d4cc39f02e05ce95a69c7500c29f6bb415c11e4e0cdb410d0ec2644d6243db38e893c8a3707
    e2=0xf493f7d1
    c2=0xd32dfad68d790022758d155f2d8bf46bb762ae5cc17281f2f3a8794575ec684819690b22106c1cdaea06abaf7d0dbf841ebd152be51528338d1da8a78f666e0da85367ee8c1e6addbf590fc15f1b2182972dcbe4bbe8ad359b7d15febd5597f5a87fa4c6c51ac4021af60aeb726a3dc7689daed70144db57d1913a4dc29a2b2ec34c99c507d0856d6bf5d5d01ee514d47c7477a7fb8a6747337e7caf2d6537183c20e14c7b79380d9f7bcd7cda9e3bfb00c2b57822663c9a5a24927bceec316c8ffc59ab3bfc19f364033da038a4fb3ecef3b4cb299f4b600f76b8a518b25b576f745412fe53d229e77e68380397eee6ffbc36f6cc734815cd4065dc73dcbcb
    Common_e_Attack(n,e1,e2,c1,c2)


    return 0;

    
if __name__ =='__main__':
    main()