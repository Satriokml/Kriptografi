import numpy as np
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def matrix2bytes(matrix):
    arr=np.array(matrix)
    return arr.flatten()

m1=matrix2bytes(state)
m2=matrix2bytes(round_key)

def add_round_key(s, k):
    for i in range(16):
        s[i] ^= k[i]
    return s 


print(add_round_key(m1, m2))

