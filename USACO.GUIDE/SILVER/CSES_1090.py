n, x = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

i = 0
j = n-1

c = 0

while i <= j:
    if i == j:
        c += 1
        break
    elif arr[i] + arr[j] > x:
        c += 1 
        j -= 1
    elif arr[i] + arr[j] <= x:
        i += 1
        j -= 1
        c += 1

print(c)