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


htmlFile = open('programmingNo3.html', 'r')
text = ''

while True:
    line = htmlFile.readline()
    if not line:
        break
    text = text + line

mailto = 'mailto'

k = 0
m = len(mailto)
n = len(text)


while True:
    pos = bruteForce(mailto, text, k)
    k = pos + m
    if k <= n :
        i = k + 1
        while True:
            if text[i] != '"':
                print(text[i], end = '')
                i += 1
            else:
                break
        print(" ")
    else:
        break
