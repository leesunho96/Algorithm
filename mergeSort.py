def merge(a, l, m, r):
    i = l
    j = m + 1
    k = l
    while i <= m and j <= r:
        if a[i] < a[j]:
            b[k] = a[i]
            k += 1
            i+=1
        else:
            b[k] = a[j]
            k+=1
            j+=1
    if i > m:
        for p in range (j, r):
            b[k] = a[p]
            k+=1
    else:
        for p in range(i, m):
            b[k] = a[p]
            k+=1
    for p in range(l, r):
        a[p] = b[p]

def mergeSort(a, l, r):
    if r > l:
        m = int((r + 1) / 2)
        
        mergeSort(a, l, m)
        mergeSort(a, m + 1, r)
        merge(a, l, m, r)



a = [None, 6, 2, 8, 1, 3, 9, 4, 5, 10, 7]
b = a.copy()
mergeSort(a, 1, 10)
