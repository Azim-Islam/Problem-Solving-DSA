from collections import defaultdict, deque

def solve(x, n, arr):
    d = defaultdict(deque)
    for i, v in enumerate(arr):
        d[(v%2)^x].append(i)
    if abs(len(d[0]) - len(d[1])) > 1:
        return -2
    d[0].reverse()
    d[1].reverse()
    i = 0
    ans = 0
    while i < n:
        if not d[i%2]:
            return float('inf')
        ans += abs(d[i%2][-1] - i)
        d[i%2].pop()
        i += 1
    return ans

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    print(min(solve(0, n, arr), solve(1, n, arr))//2)
