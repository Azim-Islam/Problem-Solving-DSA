r, c = map(int, input().split())
if r%2 == 1:
    print(r//2*10+(c-1)*2)
else:
    print((r-1)//2*10+(c-1)*2+1)