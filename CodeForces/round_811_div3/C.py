import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    ans = []
    k = 9
    while n > 9:
        n = n - k
        ans.append(k)
        k -= 1

    if n in ans:
        k = ans[-1] - 1
        while n-k >= 0 and k >= 1:
            n = n - k
            ans.append(k)
            k -= 1
        if n > 0:
            ans.append(n)

    else:
        ans.append(n)
    print("".join([str(i) for i in ans[::-1]]))