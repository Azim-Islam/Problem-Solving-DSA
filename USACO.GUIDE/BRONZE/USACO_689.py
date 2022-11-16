input = open('cowtip.in', 'r').readline
print = lambda x : open('cowtip.out', 'w').write(str(x)+'\n')

def flip(arr, r, c):
    for r0 in range(r, -1, -1):
        for c0 in range(c, -1, -1):
            if arr[r0][c0] == "1":
                arr[r0][c0] = "0"
            else:
                arr[r0][c0] = "1"

n = int(input())
arr = []
for i in range(n):
    arr.append(list(input().strip()))

count = 0
for r in range(n-1, -1, -1):
    for c in range(n-1, -1, -1):
        if arr[r][c] == "1":
            flip(arr, r, c)
            count += 1

# print(arr)
print(count)