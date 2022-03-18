from dataclasses import dataclass


data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
byte = bytearray.fromhex(data)
for x in range(256):
    ans=[chr(n^x) for n in byte]
    flag = "".join(ans)

    if flag.startswith("crypto"):
        print(flag)