input = open('mountains.in', 'r').readline
fout = open('mountains.out', 'w')

n = int(input())
arr = []

# def calcBase(x, y):
#     print(x, y, end=" = ")
#     print(x-y)
#     return y/1

for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: [x[0] - x[1], -x[1]])

i = 0
j = 1
ans = 1


while i < n and j < n:
    x0 = arr[i][0]
    y0 = arr[i][1]

    x1 = arr[j][0]
    y1 = arr[j][1] 

    bs0 = x0 - y0
    be0 = x0 + y0

    bs1 = x1 - y1
    be1 = x1 + y1 
    if bs0 <= bs1 and be0 >= be1:
        j += 1
    else:
        # print(x0, y0, x1, y1)
        # print(bs0, bs1, be0, be1)
        ans += 1
        i = j
        j += 1

print(ans, file=fout)