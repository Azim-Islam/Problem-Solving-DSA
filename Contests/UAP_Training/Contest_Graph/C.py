n = int(input())
m = [[0 for i in range(n+1)] for j in range(n+1)]
def fcost(m):
    node = 1
    f_c = 0
    f_b = 0
    for _ in range(n):
        for i in range(1, n+1):
            if m[node][i]:
                f_b += m[node][i]
                m[node][i] = 0
                node = i
                break
        else:
            for i in range(1, n+1):
                if m[i][node]:
                    f_c += m[i][node]
                    m[i][node] = 0
                    node = i
                    break
    return min(f_c, f_b)

for i in range(n):
    u, v, w = map(int, input().split())
    m[u][v] = w

print(fcost(m))
