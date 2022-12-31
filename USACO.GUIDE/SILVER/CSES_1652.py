import sys
input = sys.stdin.readline
n, q = map(int, input().split())
arr = [[0 for i in range(n+1)] for _ in range(n+1)]
# for i in range(n):
#     line = list(input())
#     for j, c in enumerate(line):
#         if c == "*":
#             arr[i+1][j+1] = 1

# build the prefix table
pref = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    line = input()
    for j in range(1, n+1):
        if line[j-1] == "*":
            t = 1
        else: t = 0
        pref[i][j] += pref[i-1][j] + pref[i][j-1] + t - pref[i-1][j-1]

ans = []
for _ in range(q):
    y1, x1, y2, x2 = map(int, input().split())
    ans.append(pref[y2][x2] - pref[y2][x1-1] - pref[y1-1][x2] + pref[y1-1][x1-1])

print("\n".join(map(str, ans)))