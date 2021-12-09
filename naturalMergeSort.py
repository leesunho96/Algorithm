N = 100000
sorting_arr = []
sorted_arr = []
run = []

def naturalMergeSort():
    cnt  = makerun()
    while cnt > 1:
        if ((cnt % 2) != 0):
            num = cnt - 1
        else:
            num = cnt
        for i in range(1, num + 1, 2):
            merge(run[i - 1] - 1, run[i], run[i + 1])
        cnt = moverun(cnt)



def makerun():
    run_num = 1
    for i in range(1, N - 1):
        if sorting_arr[i] < sorting_arr[i + 1]:
            run[run_num] = i
            run_num += 1
    return run_num - 1


def merge(l, m, r):
   
    for i in range(m + 1, l, -1):
        sorted_arr[i - 1] = sorting_arr[i - 1]
    
    for j in range(m, r):
        sorted_arr[r+m-j] = sorting_arr[j + 1]
        


def moverun(cnt):
    j = 1
    for i in range(2, cnt + 1, 2):
        run[j] = run[i]
        j += 1
    if (cnt % 2) != 0:
        run[j] = run[i - 1]
    else:
        j -= 1

    return j




import random, time

sorting_arr.append(0)
sorted_arr.append(0)

for i in range(1, N + 1):
    sorting_arr.append(random.randint(1, N))
    sorted_arr.append(0)
    run.append(0)

start_time = time.time()
naturalMergeSort()
natural_end_time = time.time() - start_time
print('자연합병 소요 시간(N = %d): %0.3f'%(N, natural_end_time))
