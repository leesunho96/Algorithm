def merge_sort(a, l, r):
    if r > l:
        print(a)
        print('\n')
        mid = (r + l) // 2
        merge_sort(a, l, mid)
        merge_sort(a, mid+1, r)
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


def check_sort(a, n):
    is_sorted = True
    for i in range(1, n):
        if a[i] > a[i+1]:
            is_sorted = False
        if not is_sorted:
            break
    if is_sorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")

import random, time

a = [None, 6, 2, 8, 1, 3, 9, 4, 5, 10, 7]
b = a.copy()

merge_sort(a, 1, 10)

check_sort(a, 10)
print(a)
