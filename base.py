import base64
import base58
import base92
import base36
import base62
import hashlib
import libnum
def main():
    c='flag{base64_base32_base16}'
    print base64.b16encode(c)
    print base64.b64encode(base64.b32encode(base64.b16encode(c)))
    print base64.b32encode(c)
    print base64.b16decode(c)
    print base58.b58encode(c)
    print base92.b92encode(c)
    print base36.loads(c)
    print base62.encodebytes(c)
    print hashlib.md5(c).hexdigest()
    

    
    return 0

if __name__=='__main__':
    main()
