# input = open('pairup.in', 'r').readline
# fout = open('pairup.out', 'w')

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[1])

i = 0
j = n-1
ans = 0
while i <= j:
    print(arr[i][0], arr[j][0])
    t = min(arr[i][0], arr[j][0]) 
    arr[i][0] -= t 
    arr[j][0] -= t
    ans = max(ans, arr[i][1]+arr[j][1])
    if arr[i][0] <= 0:
        i += 1
    if arr[j][0] <= 0:
        j -= 1

print(ans, file=fout)