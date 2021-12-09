def enqueue(queue, data):
    queue.append(data)

def dequeue(queue):
    if len(queue) == 0:
        print('queue가 공백임')
        return -1
    else:
        data = queue.pop(0)
        return data


def digit(d, k):
    temp = 1
    for i in range(1, k):
        temp *= 10
    d = int(d/temp)
    d %= 10
    return d

def radixSort(a, n, m, queue):
    for k in range(1, m + 1):
        for i in range(1, n + 1):
            kd = digit(a[i], k)
            enqueue(queue[kd], a[i])
        p = 0
        for i in range(10):
            while len(queue[i]) != 0:
                p += 1
                a[p] = dequeue(queue[i])


import random, time

radixarr = []
Q = []
M = 5

N = 1000000
radixarr.append(-1)
for i in range(1, N):
    radixarr.append(random.randint(1, 99999))
for i in range(10):
    Q.append([])

start_time = time.time()
radixSort(radixarr, N, M, Q)
end_time = time.time() - start_time

print('기수 정렬의 실행 시간(N=%d) : %0.3f' %(N, end_time))
sortingarr.clear()