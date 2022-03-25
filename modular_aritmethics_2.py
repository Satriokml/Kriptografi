r=65536
a=273246787654
p=65537

if (r==(p-1)):
    print("1")

else:
    print((a^r)%p)