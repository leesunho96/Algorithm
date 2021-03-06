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


def heapify(a, h, m):
    v, j = a[h],2 * h
    while j <= m:
        if j < m and a[j] < a[j + 1]:
            j+=1
        if v >= a[j]:
            break
        else:
            a[int(j / 2)] = a[j]
        j *= 2
    a[int(j / 2)] = v

def heapSort(a, n):
    for i in range (n//2, 0, -1):
        heapify(a, i, n)
    for i in range(n-1, 0, -1):
        a[1], a[i+1] = a[i+1], a[1]
        heapify(a, 1, i)

def merge_sort(a, b, l, r):
    if r > l:
        mid = (r + l) // 2
        merge_sort(a, b, l, mid)
        merge_sort(a, b, mid+1, r)
        for i in range(mid+1, l, -1):
            b[i-1] = a[i-1]
        i -= 1
        for j in range(mid, r):
            b[r+mid-j] = a[j+1]
        j += 1
        for k in range(l, r+1):
            if b[i] < b[j]:
                a[k] = b[i]
                i += 1
            else:
                a[k] = b[j]
                j -= 1

import random, time
import sys
sys.setrecursionlimit(10000)
arr_quickSort = []
arr_mergeSort = []
arr_heapSort = []

def test(inputN):
    N = inputN

    arr_quickSort.append(-1)
    arr_mergeSort.append(-1)
    arr_heapSort.append(-1)

    for i in range(N):
        arr_heapSort.append(random.randint(1, N))
        arr_mergeSort.append(random.randint(1, N))
        arr_quickSort.append(random.randint(1, N))

    arr_mergeCopy = arr_mergeSort.copy()
        
    start_time = time.time()
    quicksort(arr_quickSort, 1, N)
    quickSort_time = time.time() - start_time
    print('퀵 정렬의 소요시간 (N = %d) : %0.3f' %(N, quickSort_time))

    start_time = time.time()
    merge_sort(arr_mergeSort, arr_mergeCopy, 1, N)
    mergeSort_time = time.time() - start_time
    print('합병 정렬의 소요시간 (N = %d) : %0.3f' %(N, mergeSort_time))

    start_time = time.time()
    heapSort(arr_heapSort, N)
    heapSort_time = time.time() - start_time 
    print('히프 정렬의 소요시간 (N = %d) : %0.3f' %(N, heapSort_time))

    arr_heapSort.clear()
    arr_mergeCopy.clear()
    arr_mergeSort.clear()
    arr_quickSort.clear()

def test_reverse(inputN):
    N = inputN

    arr_quickSort.append(-1)
    arr_mergeSort.append(-1)
    arr_heapSort.append(-1)

    for i in range(N):
        arr_heapSort.append(random.randint(1, N))
        arr_mergeSort.append(random.randint(1, N))
    



    arr_mergeCopy = arr_mergeSort.copy()

    start_time = time.time()
    merge_sort(arr_mergeSort, arr_mergeCopy, 1, N)
    mergeSort_time = time.time() - start_time

    start_time = time.time()
    heapSort(arr_heapSort, N)
    heapSort_time = time.time() - start_time 

    start_time = time.time()
   
    quicksort_tme = time.time() - start_time

    arr_heapSort.clear()
    arr_mergeCopy.clear()
    arr_mergeSort.clear()
    arr_quickSort.clear()

    arr_mergeSort.append(-1)
    arr_heapSort.append(-1)

    for i in range(N):
        arr_heapSort.append(N-i)
        arr_mergeSort.append(N-i)

        

    arr_mergeCopy = arr_mergeSort.copy()

    start_time = time.time()
    merge_sort(arr_mergeSort, arr_mergeCopy, 1, N)
    reverse_mergeSort_time = time.time() - start_time
    start_time = time.time()
    heapSort(arr_heapSort, N)
    reverse_heapSort_time = time.time() - start_time 


    print('입력값이 랜덤인 합병 정렬의 소요시간 (N = %d) : %0.3f' %(N, mergeSort_time))
    print('입력값이 내림차순으로 정렬된(역순) 합병 정렬의 소요시간 (N = %d) : %0.3f' %(N, reverse_mergeSort_time))
    print('입력값이 랜덤인 히프 정렬의 소요시간 (N = %d) : %0.3f' %(N, heapSort_time))
    print('입력값이 내림차순으로 정렬된(역순) 히프 정렬의 소요시간 (N = %d) : %0.3f' %(N, reverse_heapSort_time))


def test_sorted(inputN):
    N = inputN
    arr_mergeSort.append(-1)
    arr_heapSort.append(-1)

    for i in range(N):
        arr_heapSort.append(i)
        arr_mergeSort.append(i)


    arr_mergeCopy = arr_mergeSort.copy()

    start_time = time.time()
    merge_sort(arr_mergeSort, arr_mergeCopy, 1, N)
    mergeSort_time = time.time() - start_time
    print('입력값이 랜덤인 합병 정렬의 소요시간 (N = %d) : %0.3f' %(N, mergeSort_time))

    start_time = time.time()
    merge_sort(arr_mergeSort, arr_mergeCopy, 1, N)
    mergeSort_time = time.time() - start_time
    print('입력값이 오름차순으로 정렬된 합병 정렬의 소요시간 (N = %d) : %0.3f' %(N, mergeSort_time))

    start_time = time.time()
    heapSort(arr_heapSort, N)
    heapSort_time = time.time() - start_time 
    print('입력값이 랜덤인 히프 정렬의 소요시간 (N = %d) : %0.3f' %(N, heapSort_time))

    start_time = time.time()
    heapSort(arr_heapSort, N)
    heapSort_time = time.time() - start_time 
    print('입력값이 오름차순으로 정렬된 히프 정렬의 소요시간 (N = %d) : %0.3f' %(N, heapSort_time))




    arr_heapSort.clear()
    arr_mergeCopy.clear()
    arr_mergeSort.clear()



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

    start_time = time.time()
    quicksort(a, 1, N)
    end_time = time.time() - start_time
    print('입력값이 오름차순인(정순) 퀵 정렬의 소요시간 (N = %d) : %0.3f)' %(N, end_time))

    a.clear()
    a.append(-1)

    for i in range(N):
        a.append(N-i)

    start_time = time.time()
    quicksort(a, 1, N)
    end_time = time.time() - start_time
    print('입력값이 내림차순으로(역순) 정렬된 퀵 정렬의 소요시간 (N = %d) : %0.3f)' %(N, end_time))

    a.clear()

for i in range(10000, 30001, 10000):
    test(i)
    test_reverse(i)
    test_sorted(i)

for i in range(1000, 3001, 1000):
    test_quicksort(i)