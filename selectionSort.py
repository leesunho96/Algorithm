import random
import time


def selectionSort(arrInput, n):
    for i in range(1, n):
        minIndex = i
        for j in range (i + 1, n + 1):
            if(arrInput[j] < arrInput[minIndex]):
                minIndex = j
            arrInput[i], arrInput[minIndex] = arrInput[minIndex], arrInput[i]
          


iList1 = [random.randint(1, 5000) for i in range(2000000)]
iList1[0] = len(iList1)
start_time = time.time()
temp = iList1[0]
selectionSort(iList1, temp-1)
end_time = time.time()

print(end_time)
