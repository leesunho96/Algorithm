def exchangeSort(inputarr, index):
    for i in range(1, index):        
         for j in range(i + 1, index):
            if inputarr[i] < inputarr[j]:
                inputarr[i], inputarr[j] = inputarr[j], inputarr[i]


def selectionSort(arrInput, n):
    for i in range(1, n):
        minIndex = i
        for j in range (i + 1, n + 1):
            if arrInput[j] > arrInput[minIndex]:
                minIndex = j
            arrInput[i], arrInput[minIndex] = arrInput[minIndex], arrInput[i]

def bubbleSort(inputArr, iSize):
	for i in range(iSize, 0, -1):
		for j in range (1, i):
			if inputArr[j] < inputArr[j+1]:
				inputArr[j], inputArr[j + 1] = inputArr[j+1], inputArr[j]


import time
import random

N = 5000
selectArr = []
bubbleArr = []
exchangeArr = []

selectArr.append(None)
bubbleArr.append(None)
exchangeArr.append(None)

for i in range (N):
    temp = i
    exchangeArr.append(temp)
    selectArr.append(temp)
    bubbleArr.append(temp)
    
start_time = time.time()
selectionSort(selectArr, N)
sel_time = time.time() - start_time

start_time = time.time()
bubbleSort(bubbleArr, N)
bub_time = time.time() - start_time

start_time = time.time()
exchangeSort(exchangeArr, N)
exchange_time = time.time() - start_time



print('선택정렬 실행시간(N = %d) : %0.3f)' %(N, sel_time))
print('버블정렬 실행시간(N = %d) : %0.3f)' %(N, bub_time))
print('교환정렬 실행시간(N = %d) : %0.3f)' %(N, exchange_time))


selectArr.clear()
bubbleArr.clear()
exchangeArr.clear()

N = 10000
selectArr = []
bubbleArr = []
exchangeArr = []

selectArr.append(None)
bubbleArr.append(None)
exchangeArr.append(None)

for i in range (N):
    temp = i
    exchangeArr.append(temp)
    selectArr.append(temp)
    bubbleArr.append(temp)
    
start_time = time.time()
selectionSort(selectArr, N)
sel_time = time.time() - start_time

start_time = time.time()
bubbleSort(bubbleArr, N)
bub_time = time.time() - start_time

start_time = time.time()
exchangeSort(exchangeArr, N)
exchange_time = time.time() - start_time



print('선택정렬 실행시간(N = %d) : %0.3f)' %(N, sel_time))
print('버블정렬 실행시간(N = %d) : %0.3f)' %(N, bub_time))
print('교환정렬 실행시간(N = %d) : %0.3f)' %(N, exchange_time))


selectArr.clear()
bubbleArr.clear()
exchangeArr.clear()

N = 15000
selectArr = []
bubbleArr = []
exchangeArr = []

selectArr.append(None)
bubbleArr.append(None)
exchangeArr.append(None)

for i in range (N):
    temp = i
    exchangeArr.append(temp)
    selectArr.append(temp)
    bubbleArr.append(temp)
    
start_time = time.time()
selectionSort(selectArr, N)
sel_time = time.time() - start_time

start_time = time.time()
bubbleSort(bubbleArr, N)
bub_time = time.time() - start_time

start_time = time.time()
exchangeSort(exchangeArr, N)
exchange_time = time.time() - start_time



print('선택정렬 실행시간(N = %d) : %0.3f)' %(N, sel_time))
print('버블정렬 실행시간(N = %d) : %0.3f)' %(N, bub_time))
print('교환정렬 실행시간(N = %d) : %0.3f)' %(N, exchange_time))


selectArr.clear()
bubbleArr.clear()
exchangeArr.clear()
