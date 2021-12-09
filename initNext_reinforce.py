def initNext(p, m):
    m = len(p)
    next[0] = -1
    i = 0
    j = -1
    
    while i < M:
        if j != -1 and p[i] == p[j]:
            next[i] = next[j]
        else:
            next[i] = j
        
        while j >= 0 and p[i] != p[j]:
            j = next[j]
            
        i += 1
        j += 1

while True:
    next = [0] * 50
    pattern = input('문자열 : ')
    M = len(pattern)
    initNext_improved(pattern, M)

    for i in range(1, M):
        print(next[i], end=' ')
    next.clear()
    print(" ")