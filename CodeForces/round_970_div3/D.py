from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    arr = [0]+list(map(int, input().split()))
    color = [-1] + list(map(int, list(input())))
    dp = defaultdict(set)
    blacks = defaultdict(set)
    # dfs 
    ans = []
    for i in range(1, n+1):
        if dp[i]:
            # ans.append(len(blacks[i]))
            pass
        else:
            visited = set()
            black = set()

            dp[i] = visited
            blacks[i] = black
            visited.add(i)
            if not color[i]:
                black.add(i)

            stack = [i]
            while stack:
                v = stack.pop()
                next = arr[v]
                if next not in visited:
                    visited.add(next)
                    stack.append(next)
                    dp[next] = visited
                    blacks[next] = black
                if not color[next]:
                    black.add(next)
        # print(blacks[i], dp[i])
        ans.append(len(blacks[i]))
    print(*ans)
