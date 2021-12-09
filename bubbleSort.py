def bubbleSort(inputArr, iSize):
	for i in range(iSize, 0, -1):
		for j in range (1, i):
			if (inputArr[j] > inputArr[j+1]):
				inputArr[j], inputArr[j + 1] = inputArr[j+1], inputArr[j]


a[5] = (3, 2, 1, 4, 5)
bubbleSort(a, 5)

