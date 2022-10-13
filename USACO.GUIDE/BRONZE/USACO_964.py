# input = open('whereami.in', 'r').readline
# print = lambda x : open('whereami.out', 'w').write(str(x)+'\n')


n = int(input())
arr = input().rstrip()

def sol(arr):
    for k in range(1, n):
        s = set()
        for i in range(n-k+1):
            s.add(arr[i:i+k])
            print(i, k, arr[i:i+k])
        # print(s)
        if len(s) == n-k+1:
            return k

print(sol(arr))