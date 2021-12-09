def cocktailShakerSort(inputarr, index):
    right = 1
    left = index - 1

    while(right < left):
        for i in range (right, left):
            if (inputarr[i] > inputarr[i + 1]):
                inputarr[i], inputarr[i + 1] = inputarr[i + 1], inputarr[i]
        
        left -= 1
        for i in range (left, right, -1):
            if (inputarr[i] < inputarr[i -1]):
                inputarr[i], inputarr[i - 1] = inputarr[i - 1], inputarr[i]
        right += 1

def bubbleSort(inputArr, iSize):
	for i in range(iSize - 1, 0, -1):
		for j in range (1, i):
			if (inputArr[j] > inputArr[j+1]):
				inputArr[j], inputArr[j + 1] = inputArr[j+1], inputArr[j]

def issort(arr):    
    for i in range(0, len(arr)):
        if arr[i] > arr[i + 1]:
            print("error")       
                     
import random, time

cocktailArr = []
bubblearr = []

N = 50
cocktailArr.append(None)
for i in range(1, N):
    cocktailArr.append(random.randint(1, N))

bubblearr = cocktailArr.copy()



start_time = time.time()
cocktailShakerSort(cocktailArr, N)
cocktail_end_time = time.time() - start_time

print(cocktailArr)
