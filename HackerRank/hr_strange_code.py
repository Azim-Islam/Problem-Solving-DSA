t = int(input())
strt = 3 
i = 0
while strt*2-2 <= t:
    strt = strt*2
ans = (strt-2) - (t-strt)
print(ans)