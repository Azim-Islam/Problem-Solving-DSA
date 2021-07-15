n, k = map(int, input().split())
contest = [[],[]]
for _ in range(n):
    l, t = map(int, input().split())
    contest[t].append(l)
saved_luck = sum(contest[0])
contest[1].sort(reverse=True)
saved_luck += sum(contest[1][0:k]) - sum(contest[1][k:])
print(saved_luck)