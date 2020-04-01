from Crypto.Cipher import AES
import base64
a = base64.b64decode(open('s1c7.txt').read())
print(len(a))
obj = AES.new(b'YELLOW SUBMARINE', AES.MODE_ECB)
print(obj.decrypt(a))
