class bitskey:
    def __init__(self, x):
        self.x = x

    def get(self):
        return self.x

    def bits(self, k, j):
        return (self.x >> k) & ~(~0 << j)


def allbit(iinput):
    temp = bitskey(iinput)
    for i in range(5, -1, -1):
        print(temp.bits(i, 1), end = '')
    print("")

while(True):
    x = int(input("정수 입력 하세요(종료 : -1) :"))
    if x == -1:
        break
    allbit(x)
