from numpy import char


string = [ord(c) for c in 'label']
lst = []
for x in string:
    x ^= 13
    lst.append(x)
list = [chr(a) for a in lst]
print (list)
