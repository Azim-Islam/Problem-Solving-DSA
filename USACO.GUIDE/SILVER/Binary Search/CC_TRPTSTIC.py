def check_sum(DP, dist, i, j, K, N, M):
    i0 = max(0, i-dist-1)
    j0 = max(0, j-dist-1)
    i  = min(N, i+dist)
    j = min(M, j+dist)

    s = DP[i][j] - DP[i0][j] - DP[i][j0] + DP[i0][j0]
    if s >= K:
        return 1
    return 0

def check(MAP, DP, dist, N, M, K):
    for i in range(1, N+1):
        for j in range(1, M+1):
            if MAP[i-1][j-1]:
                if check_sum(DP, dist, i, j, K, N, M):
                    return 1
    return 0





for _ in range(int(input())):
    N, M, K = map(int, input().split())
    DP = [[0]*(M+1) for _ in range(N+1)]
    MAP = []
    for i in range(N):
        MAP.append(list(map(int, input().split())))
    
    for i in range(1, N+1):
        for j in range(1, M+1):
            DP[i][j] = MAP[i-1][j-1] + DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1]

    lo = 0
    hi = 10**9
    K = K+1
    if DP[-1][-1] < K:
        print("-1")
    else:
        while lo < hi:
            mid = (lo + hi)//2
            if check(MAP, DP, mid, N, M, K):
                hi = mid
            else:
                lo = mid + 1

        print(hi)