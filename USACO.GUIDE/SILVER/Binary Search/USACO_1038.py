input = open("socdist.in", "r").readline
out = open('socdist.out', 'w')

def check(arr, c, d):
    last = arr[0][0]
    c -= 1
    for start, end in arr:
        if last+d < start:
            last = start
            c -= 1
        while last+d <= end:
            last += d
            c -= 1

    if c <= 0:
        return 1
    return 0


n, m = map(int, input().split())

arr = []

for i in range(m):
    arr.append(list(map(int, input().split())))


arr.sort()

#Binary Search 

lo = 1; hi = 10**18

while lo < hi:
    mid = (lo+hi+1)//2
    if check(arr, n, mid):
        lo = mid
    else:
        hi = mid - 1

# check(arr, n, 2)

print(lo, file=out)
