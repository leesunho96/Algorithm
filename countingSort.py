def countingSort(inputarr, num, m):
    sortedarr = [0] * (num + 1)
    count = [0] * (m + 1)
    for j in range(1, m + 1):
        count[j] = 0
    for i in range(1, num + 1):
        count[inputarr[i]] += 1
    for j in range(2, m + 1):
        count[j] += count[j - 1]
    for i in range(num, 0, -1):
        sortedarr[count[inputarr[i]]] = inputarr[i]
        count[inputarr[i]] -= 1
    for j in range(1, num + 1):
        inputarr[j] = sortedarr[j]


import random, time

sortingarr = []
M = 1000

N = 1000000
sortingarr.append(None)
for i in range(1, N):
    sortingarr.append(random.randint(1, M))

start_time = time.time()
countingSort(sortingarr, N, M)
end_time = time.time() - start_time

print('계수 정렬의 실행 시간(N=%d) : %0.3f' %(N, end_time))
sortingarr.clear()

N = 2000000
sortingarr.append(None)
for i in range(1, N):
    sortingarr.append(random.randint(1, M))

start_time = time.time()
countingSort(sortingarr, N, M)
end_time = time.time() - start_time

print('계수 정렬의 실행 시간(N=%d) : %0.3f' %(N, end_time))
sortingarr.clear()

N = 3000000
sortingarr.append(None)
for i in range(1, N):
    sortingarr.append(random.randint(1, M))

start_time = time.time()
countingSort(sortingarr, N, M)
end_time = time.time() - start_time

print('계수 정렬의 실행 시간(N=%d) : %0.3f' %(N, end_time))
sortingarr.clear()
