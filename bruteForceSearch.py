def bruteForce(inputString, inputText, startPoint):
    M = len(inputString)
    N = len(inputText)
    i = startPoint
    j = 0
    while j < M and i < N:
        if inputText[i] != inputString[j]:
            i -= j
            j = -1

        i += 1
        j += 1
    if j == M:
        return i - M
    else:
        return i

text = "zxcvzxcvzxcvzxcv"
searchintText = "zxcv"

m = len(searchintText)
n = len(text)
k = 0

print("입력 문자열 : ", text)
print("탐색 문자열 : ", searchintText)
while True:
    pos = bruteForce(searchintText, text, k)
    k = pos + m
    if k <= n :
        print('패턴 등장 위치 : ', pos)
    else:
        break

print("문자열 탐색 종료")
            