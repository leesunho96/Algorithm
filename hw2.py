def selectionSort(arrInput, n):
    for i in range(1, n):
        minIndex = i
        for j in range (i + 1, n + 1):
            if(arrInput[j] < arrInput[minIndex]):
                minIndex = j
            arrInput[i], arrInput[minIndex] = arrInput[minIndex], arrInput[i]

def bubbleSort(inputArr, iSize):
	for i in range(iSize, 0, -1):
		for j in range (1, i):
			if (inputArr[j] > inputArr[j+1]):
				inputArr[j], inputArr[j + 1] = inputArr[j+1], inputArr[j]

def insertionSort(a, iSize):
    for i in range(2, iSize + 1):
        a[0] = a[i]
        j = i
        while a[j - 1] > a[0]:
            a[j] = a[j - 1]
            j = j - 1
        a[j] = a[0]

def shellSort(a, n):
    h = 1
    while h < n:
        h = 3 * h + 1
    while h > 0:
        for i in range(h+1, n+1):
            v, j = a[i], i
            while j > h and a[j - h] > v:
                a[j] = a[j - h]
                j -= h
            a[j] = v
        h = int(h / 3)


import time
import random


def test_random(inputN):
    N = inputN
    selectArr = []
    bubbleArr = []
    insertArr = []
    shellArr = []

    selectArr.append(None)
    bubbleArr.append(None)
    insertArr.append(-1)
    shellArr.append(-1)

    for i in range (N):
        selectArr.append(random.randint(1, N))
        bubbleArr.append(random.randint(1, N))
        insertArr.append(random.randint(1, N))
        shellArr.append(random.randint(1, N))

    start_time = time.time()
    selectionSort(selectArr, N)
    sel_time = time.time() - start_time

    start_time = time.time()
    bubbleSort(bubbleArr, N)
    bub_time = time.time() - start_time

    start_time = time.time()
    insertionSort(insertArr, N)
    insert_time = time.time() - start_time

    start_time = time.time()
    shellSort(shellArr, N)
    shell_time = time.time() - start_time

    print('선택정렬 실행시간(N = %d) : %0.3f)' %(N, sel_time))
    print('버블정렬 실행시간(N = %d) : %0.3f)' %(N, bub_time))
    print('삽입정렬 실행시간(N = %d) : %0.3f)' %(N, insert_time))
    print('쉘정렬 실행시간(N = %d) : %0.3f)' %(N, shell_time))

    selectArr.clear()
    bubbleArr.clear()
    insertArr.clear()
    shellArr.clear()

def test_reverse(inputN):
    N = inputN
    selectArr = []
    bubbleArr = []
    insertArr = []
    shellArr = []

    selectArr.append(None)
    bubbleArr.append(None)
    insertArr.append(-1)
    shellArr.append(-1)

    for i in range (N):
        selectArr.append(N-i)
        bubbleArr.append(N-i)
        insertArr.append(N-i)
        shellArr.append(N-i)


    start_time = time.time()
    selectionSort(selectArr, N)
    sel_time = time.time() - start_time

    start_time = time.time()
    bubbleSort(bubbleArr, N)
    bub_time = time.time() - start_time

    start_time = time.time()
    insertionSort(insertArr, N)
    insert_time = time.time() - start_time

    start_time = time.time()
    shellSort(shellArr, N)
    shell_time = time.time() - start_time

    print('역순으로 정렬된 리스트의 선택정렬 실행시간(N = %d) : %0.3f)' %(N, sel_time))
    print('역순으로 정렬된 리스트의 버블정렬 실행시간(N = %d) : %0.3f)' %(N, bub_time))
    print('역순으로 정렬된 리스트의 삽입정렬 실행시간(N = %d) : %0.3f)' %(N, insert_time))
    print('역순으로 정렬된 리스트의 쉘정렬 실행시간(N = %d) : %0.3f)' %(N, shell_time))

    selectArr.clear()
    bubbleArr.clear()
    insertArr.clear()
    shellArr.clear()

def test_order(inputN):
    N = inputN
    selectArr = []
    bubbleArr = []
    insertArr = []
    shellArr = []

    selectArr.append(None)
    bubbleArr.append(None)
    insertArr.append(-1)
    shellArr.append(-1)

    for i in range (N):
        selectArr.append(i)
        bubbleArr.append(i)
        insertArr.append(i)
        shellArr.append(i)


    start_time = time.time()
    selectionSort(selectArr, N)
    sel_time = time.time() - start_time

    start_time = time.time()
    bubbleSort(bubbleArr, N)
    bub_time = time.time() - start_time

    start_time = time.time()
    insertionSort(insertArr, N)
    insert_time = time.time() - start_time

    start_time = time.time()
    shellSort(shellArr, N)
    shell_time = time.time() - start_time

    print('정렬된 리스트의 선택정렬 실행시간(N = %d) : %0.3f)' %(N, sel_time))
    print('정렬된 리스트의 버블정렬 실행시간(N = %d) : %0.3f)' %(N, bub_time))
    print('정렬된 리스트의 삽입정렬 실행시간(N = %d) : %0.3f)' %(N, insert_time))
    print('정렬된 리스트의 쉘정렬 실행시간(N = %d) : %0.3f)' %(N, shell_time))

    selectArr.clear()
    bubbleArr.clear()
    insertArr.clear()
    shellArr.clear()

for i in range(5000, 15001, 5000):
    test_random(i)
    test_reverse(i)
    test_order(i)

