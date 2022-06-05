inputs = open('cbarn.in', 'r')
print = lambda x : open('cbarn.out', 'w').write(str(x)+'\n')

N = int(inputs.readline())
arr = [int(inputs.readline()) for i in range(N)]
ans = [0]*N

for i, v in enumerate(arr):
    for j, v in enumerate(arr):
        if i > j:
            ans[i] += v*abs(N-i+j)
        else:
            ans[i] += v*abs(i-j)
print(min(ans))