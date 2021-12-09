class Dict:
    def __init__(self, M):
        Dict.a = [-1] * M

    def search(self, v, M):
        x = self.hash(v, M)
        u = self.hash2(v)

        while Dict.a[x] != -1:
            if v == Dict.a[x]:
                return Dict.a[x]

            else:
                x = (x + u) % M

        return -1

    def insert(self, v, M):
        x = self.hash(v, M)
        u = self.hash2(v)

        while Dict.a[x] != -1:
            x = (x + u) % M
        Dict.a[x] = v

    def hash(self, v, M):
        return v % M

    def hash2(self, v):
        return 64 - (v % 64)

    def print(self, M):
        for i in range(M):
            if Dict.a[i] != -1:
                print('#', end='')

            else:
                print(' ', end='')

            if (i + 1) % 60 == 0:
                print()

import random, time

N = 10000
   
    #N = 1000
    #M = 1009
key = []
s_key = []

for i in range(N):
    r = random.randint(1, 3 * N)
    key.append(r)
    s_key.append(r)

def test(iinput):
    M = iinput

    d = Dict(M)

    for i in range(N):
        d.insert(key[i], M)

    start_time = time.time()

    for i in range(N):
        result = d.search(s_key[i], M)

        if result == -1 or result != s_key[i]:
            print('Search Error!')

    end_time = time.time() - start_time

    print('이중 해시 사용시 Time (N = %d, M = %d) : %0.3f'%(N, M,  end_time))
    print('Search Complete')
#d.print()

test(10357)
test(10369)
test(10391)
test(10399)
test(10427)
test(10429)
test(10433)
test(10453)
test(10457)
test(10459)

                                   