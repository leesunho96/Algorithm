def quicksort(a, l, r):
    if r > l:
        v = a[r]
        i = l - 1
        j = r
        while True:
            i += 1
            while a[i] < v:
                i = i + 1
            j -= 1
            while a[j] > v:
                j = j - 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]
        a[i], a[r] = a[r], a[i]
        quicksort(a, l, i - 1)
        quicksort(a, i + 1, r)

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]):
            isSorted = False
        if (not isSorted):
            break

    if(isSorted):
        print('정렬')
    else :
        print('안됨')

import random, time
import sys
sys.setrecursionlimit(10000)


def test_quicksort(inputN):
    a = []
    N = inputN
    a.append(-1)
    for i in range(N):
        a.append(random.randint(1, N))

        
    start_time = time.time()
    quicksort(a, 1, N)
    end_time = time.time() - start_time
    print('입력값이 랜덤인 퀵 정렬의 소요시간 (N = %d) : %0.3f)' %(N, end_time))
    a.clear()
    a.append(-1)

    for i in range(N):
        a.append(N-i)

    start_time = time.time()
    quicksort(a, 1, N)
    end_time = time.time() - start_time
    print('입력값이 내림차순으로(역순) 정렬된 퀵 정렬의 소요시간 (N = %d) : %0.3f)' %(N, end_time))

    a.clear()

for i in range(1000, 3001, 1000):
    test_quicksort(i)