def check(arr, k):
    min_1 = float('inf')
    min_2 = abs(arr[0]-k)
    for i in range(1, len(arr)):
        min_1 = min(min_1, abs(arr[i-1]-arr[i]))
        min_2 = max(min_2, abs(arr[i] - k))

    if min_2 <= min_1:
        return True
    return False

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(1, 101):
        if i not in arr and check(arr, i):
            print("YES")
            break
    else:
        print("NO")
