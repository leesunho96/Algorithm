class point:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c

class line:
    def __init__(self):
        self.p1 = point(None, None, None)
        self.p2 = point(None, None, None)


x_value = [8, 4, 7, 6, 5, 2, 1, 3]
y_value = [2, 1, 5, 6, 4, 3, 8, 7]
c_value = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']

_5_3x = [5, 7, 6, 8, 1, 4, 3, 2, 11, 12, 10, 9]
_5_3y = [3, 11, 12, 2, 4, 10, 6, 5, 8, 9, 1, 7]
_5_3c = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

# x_value = [5, 7, 3, 1, 9, 12, 10, 2]
# y_value = [3, 11, 10, 6, 7, 5, 4, 2]
# c_value = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']