for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    seg_size = 0
    
    for i in range(1, n):
        ans += 0 if (arr[i] > max(arr[0: i])) else 1

    print(ans)