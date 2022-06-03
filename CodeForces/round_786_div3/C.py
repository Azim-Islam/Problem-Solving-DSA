

for _ in range(int(input())):
    s = input()
    t = input()
    # counts_as = Counter(t)
    if 'a' in t and (len(t) > 1):
        print(-1)
    elif 'a' in t and len(t) == 1:
        print(1)
    else:
        ans = 0
        for i in range(1, len(s)+1):
            ans += i
        print(ans+1)