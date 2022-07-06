read = open('balancing.in', 'r').readline
write = lambda x : open('balancing.out', 'w').write(str(x))

# read = input
# write = print

def find(a, b, arr_):
    arr = [0]*4
    a, b = max(0, a), max(0, b)
    for x, y in arr_:
        if x < a and y < b:
            arr[0] += 1 
        elif x < a and y > b:
            arr[1] += 1
        elif x > a and y < b:
            arr[2] += 1
        elif x > a and y > b:
            arr[3] += 1
    return max(arr)

def f(x,y, arr_):
    ans = float('inf')
    ret = min([
        find(x-1, y-1, arr_)
        ])
    ans = min(ans, ret)
    return ans

n, b = map(int, read().split())
arr = []

for i in range(n):
    x, y = map(int, read().split())
    arr.append((x,y))

ans = float('inf')
for x in [i[0] for i in arr]:
    for y in [i[1] for i in arr]:
        ans = min(ans, f(x,y, arr))


write(ans)