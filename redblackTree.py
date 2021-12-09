black = 0
red = 1
class node:
    def __init__(self, color, key=None, left=None, right=None):
        self.color = color
        self.key = key
        self.right = right
        self.left = left

class Dict():
    x = p = q = gg = node
    z = node(color = black, key = 0, left = 0, right = 0)
    z.left = z
    z.right = z
    head = node(color = black, key = 0, left = 0, right = z)

    def search(self, search_key):
        x = self.head.right
        while x != self.z:
            if x.key == search_key:
                return x.key
            if x.key > search_key:
                x = x.left
            else:
                x = x.right
        
        return -1

 
    def check(self, arr, len):      
        print('=================================================')  
        print(arr)
        start_time = time.time()
        for i in range(0, len):
            x = self.head.right
            temp_node = x
            search_key = i
            while x != self.z:           
                if x.key == search_key:
                    if x.color == 0:
                        color_string = 'black'
                    else:
                        color_string = 'red'
                    print("key = %d, parent = %d, color = %s"%(x.key, temp_node.key, color_string))
                if x.key > search_key:
                    temp_node = x
                    x = x.left
                else:
                    temp_node = x
                    x = x.right    

        end_time = time.time() - start_time
        print('레드 블랙 트리 탐색의 실행 시간(N = %d) : %0.3f'%(len, end_time))
        print("탐색완료")
        print('=================================================')
      

    def insert(self, v):
        x = p = g = self.head
        while x != self.z:
            gg = g
            g = p
            p = x
            if x.key == v:
                return
            if x.key > v:
                x = x.left
            else:
                x = x.right

            if x.left.color and x.right.color:
                self.split(x, p, g, gg, v)
        
        x = node(color = red, key = v, left = self.z, right = self.z)
        if p.key > v:
            p.left = x
        else:
            p.right = x
        self.split(x, p, g, gg, v)
        self.head.right.color = black

    def split(self, x, p, g, gg, v):
        x.color = red
        x.left.color = black
        x.right.color = black
        
        if p.color:
            g.color = red
            if (g.key > v) != (p.key > v):
                p = self.rotate(v, g)
            x = self.rotate(v, gg)
            x.color = black

    def rotate(self, v, y):
        gc = c = node
        if y.key > v:
            c = y.left
        else:
            c = y.right
        
        if c.key > v:
            gc = c.left
            c.left = gc.right
            gc.right = c 
        else:
            gc = c.right
            c.right = gc.left
            gc.left = c

        if y.key > v:
            y.left = gc
        else:
            y.right = gc
        return gc


import random, time

def test(iNum):
    N = iNum
    key = []
    temp = (int)(N / 2)
    for i in range(0, temp):
        key.append(i + 1)
        key.append(N - i)
    s_key = list(range(1, N + 1))

   

    d = Dict()
    for i in range(0, N):
        d.insert(key[i])
    start_time = time.time()
    for i in range(N):
        result = d.search(s_key[i])
        if result == -1 or result != s_key[i]:
            print("탐색 오류")
    end_time = time.time() - start_time
    print("큰값 작은값이 번갈아 나오는 red-black Tree 탐색 실행 시간(N = %d) : %0.3f"%(N, end_time))
    print("탐색완료")


def check_test():
    N = 9
    arr = [2, 1, 8, 9, 7, 3, 6, 4, 5]
    d = Dict()
    for i in range(9):
        d.insert(arr[i])
    
    d.check(arr, N)
        
test(10000)
check_test()