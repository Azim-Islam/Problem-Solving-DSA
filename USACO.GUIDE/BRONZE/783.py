inputs = open("billboard.in", "r")
print = lambda x : open("billboard.out", "w").write(str(x)+"\n")
# print(inputs)

x1, y1, x2, y2 = map(int, inputs.readline().split())
a1, b1, a2, b2 = map(int, inputs.readline().split())



class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def area(self):
        return abs(x1-x2)*abs(y1-y2)



lawn_board = Rectangle(x1, y1, x2, y2)
food_board = Rectangle(a1, b1, a2, b2)
ans = 0
if (a1 <= x1 and b1 <= y1) and not (a2 < x2 and b2 < y2):
    res1 = (x2-a2) * abs(y1-y2)
    res2 = (y2-b2) * abs(x1-x2)
    ans = max([res1, res2, 0])
    print(ans)
elif (a2 >= x2 and b2 >= y2) and not (a1 > x1 and b1 > y1):
    res1 = (a1-x1) * abs(y1-y2)
    res2 = (b1-y1) * abs(x1-x2)
    ans = max([res1, res2, 0])
    print(ans)
else:
    print(lawn_board.area())