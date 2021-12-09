class node:
    def __init__(self, key = None, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

class Dict:
    x = p = node
    z = node(key = 0, left = 0, right = 0)
    z.left = z
    z.right = z
    head = node(key = 0, left = 0, right = z)

    def search(self, search_key):
        x = self.head.right
        while x != self.z:
            if x.key == search_key:
                print("")
                print('탐색 성공')
                return x.key
            if x.key > search_key:
                x = x.left
                print("left", end = ' ')
            else:
                x = x.right
                print("right", end = ' ')
        return -1

    def insert(self, v):
        x = p = self.head
        while (x != self.z):
            p = x
            if x.key == v:
                return
            if x.key > v:
                x = x.left
                
            else:
                x = x.right
                

        x = node(key = v, left = self.z, right = self.z)

        if p.key > v:
            p.left = x
        else:
            p.right = x

a = [2, 1, 7, 8, 6, 3, 5, 4]
d = Dict()
for i in range(len(a)):
    d.insert(a[i])

inputkey = 1
while (inputkey != 999):
    print(" ")
    inputkey = input("탐색키 입력 : ")
    inputkey = int(inputkey)
    if inputkey == 999:
        print("탐색 종료")
        break
    result = d.search(inputkey)
    if result == -1:
        print(" ")
        print("탐색실패")