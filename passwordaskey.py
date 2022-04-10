from matplotlib.pyplot import text
import requests
from Crypto.Cipher import AES
from hashlib import md5

url = "https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words"
texts = requests.get(url).text.splitlines()
ct = bytes.fromhex('c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66')

for i in texts:
    i = md5(i.encode()).digest()
    aes = AES.new(i, AES.MODE_ECB)
    dec = aes.decrypt(ct)
    if b'crypto' in dec:
        print(dec)