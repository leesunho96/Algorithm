import numpy as np
import random

def tournament_sort(a,n):
    
    c = []
    x = 2**int(np.log2(n)+1)
    b = [0] * (x*2)
    for i in range(0, n):
        b[i+x] = a[i+1]
    for i in range(x-1, 0, -1):
        
        if b[i*2] > b[i*2+1]:
            b[i] = b[i*2]
        else:
            b[i] = b[i*2+1]
    c.append(b[1])
    print(b)
    while len(c) < n:
        l = 1
        while l < x:
            if b[2 * l] == b[1]:
                l = 2*l
            else:
                l = 2*l+1
        b[l] = 0
        while l > 1:
            l = l//2
            if b[2 * l] < b[2 * l + 1]:
                b[l] = b[2 * l + 1]
            else:
                b[l] = b[2 * l]
        c.append(b[1])
        print(b)
        
    return c

N = 10000
torn_arr = [] * N

for i in range(0, N):
    torn_arr[i] = random.randint(0, N)

