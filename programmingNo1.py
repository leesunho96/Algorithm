    
def bubble_reinforced(inputarr, index):
    right = 1
    left = index - 1

    for j in range(right, left):
        if inputarr[j] % 2 == 1:
            for i in range (right, left):
                if (inputarr[i] > inputarr[i + 1]):
                    inputarr[i], inputarr[i + 1] = inputarr[i + 1], inputarr[i]
                    
            print('i =', j, inputarr)
            left -= 1
        else:
            for i in range (left, right, -1):
                if (inputarr[i] < inputarr[i - 1]):
                    inputarr[i], inputarr[i - 1] = inputarr[i - 1], inputarr[i]
            
            right += 1
            print('i =', j, inputarr)
            

a = [0, 7, 5, 6, 4, 10, 9, 8, 1, 3, 2]

bubble_reinforced(a,11)
print(a)
