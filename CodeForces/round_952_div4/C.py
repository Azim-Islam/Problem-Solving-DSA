from collections import defaultdict


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    pre = [0]
    d = defaultdict(int)
    for i in arr:
        pre.append(i+pre[-1])
    count = 0
    for i in range(n):
        d[str(arr[i])] += 1
        if pre[i+1]%2 == 0:
            count += 1 if d[str(pre[i+1]//2)] else 0

    print(count)