
def fib_dynamic(num):
    global num_dynamic
    f = [0] * (num + 1)
    f[0] = 0
    num_dynamic += 1
    if num > 0:
        f[1] = 1
        num_dynamic += 1
        for i in range(2, num + 1):
            f[i] = f[i-1] + f[i-2]
            num_dynamic += 1

    return f[num]

def fib_recursive(num):
    global num_recursive
    num_recursive += 1
    if num <= 0:
        return 0
    if num == 1:
        return 1
    else: return fib_recursive(num - 1) + fib_recursive(num - 2)



num_dynamic = 0
num_recursive = 0

a = fib_dynamic(5)
b = fib_recursive(5)

print("피보나치 수열 5번째 구하는 경우")
print('동적 계획법의 피보나치 호출 횟수(값 : %d) : %d'%(a, num_dynamic))
print('부분 정복 피보나치 수열 호출 횟수(값: %d) : %d'%(b, num_recursive))
