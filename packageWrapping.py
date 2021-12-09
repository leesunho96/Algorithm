import geo as g
def theta(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    ax = abs(dx)
    ay = abs(dy)
    
    if ax + ay == 0:
        t = 0
    else: t = dy / (ax + ay)
    if dx < 0:
        t = 2 - t
    elif dy < 0:
        t = 4 + t
    return 90 * t

def packageWrapping(p, n):
    minIndex = 0
    for i in range(n):
        if p[i].y < p[minIndex].y:
            minIndex = i
    p[n] = p[minIndex]
    th = 0.0
    for m in range(n):
        p[m], p[minIndex] = p[minIndex], p[m]
        minIndex = n
        v = th
        th = 360
        for i in range(m + 1, n + 1):
            if theta(p[m], p[i]) > v:
                if theta(p[m], p[i]) < th:
                    minIndex = i
                    th = theta(p[m], p[minIndex])
        if minIndex == n:
            return m

N = 16
p = []
x_value = [2, 12, 3, 10, 14, 1, 13, 6, 8, 7, 15, 16, 4, 11, 9, 5]
y_value = [6, 16, 12, 11, 4, 10, 8, 7, 9, 5, 3, 14, 15, 1,13, 2]
c_value = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
for i in range(N):
    p.append(g.point(x_value[i], y_value[i], c_value[i]))
p.append(g.point(None, None, None))
M = packageWrapping(p, N)
for i in range(M + 1):
    print(p[i].c, end = ' ')           
