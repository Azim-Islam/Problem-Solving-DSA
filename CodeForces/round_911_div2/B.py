from sys import stdin, stdout
ans = []
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(~(b^c)&1, ~(c^a)&1, ~(a^b)&1)
