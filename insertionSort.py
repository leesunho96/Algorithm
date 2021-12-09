def insertionSort(inputArr, iSize):
    for i in range(2, iSize + 1):
        a[0] = a[i]
        j = i
        while a[j - 1] > a[0]:
            a[j] = a[j - 1]
            j = j - 1
        a[j] = a[0]


