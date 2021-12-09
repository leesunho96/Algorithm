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

sys.setrecursionlimit(7000)

arr_quickSort = []
arr_mergeSort = []
arr_heapSort = []
N = 100000

arr_quickSort.append(-1)
arr_mergeSort.append(-1)
arr_heapSort.append(-1)

for i in range(N):
    arr_heapSort.append(i)
    arr_mergeSort.append(i)
    arr_quickSort.append(i)

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
arr_quickSort.clear()

N = 200000

arr_quickSort.append(-1)
arr_mergeSort.append(-1)
arr_heapSort.append(-1)

for i in range(N):
    arr_heapSort.append(i)
    arr_mergeSort.append(i)
    arr_quickSort.append(i)

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
arr_quickSort.clear()

N = 300000

arr_quickSort.append(-1)
arr_mergeSort.append(-1)
arr_heapSort.append(-1)

for i in range(N):
    arr_heapSort.append(i)
    arr_mergeSort.append(i)
    arr_quickSort.append(i)

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
arr_quickSort.clear()