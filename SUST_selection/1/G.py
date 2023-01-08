s, t = map(int, input().split())
c = 0

for i in range(0, 101):
    for j in range(0, 101):
        for k in range(0, 101):
            if  i+j+k <=s and i*j*k <=t:
                c += 1

print(c)