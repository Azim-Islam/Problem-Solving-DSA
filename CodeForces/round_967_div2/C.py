from sys import stdout

def solve(n):
    st = [[0 for l in range(n+1)] for k in range(n+1)]


    for i in range(1, n+1):
        st[i][i] = 1

    count = 0
    for i in range(1, n+1):
        if count >= n-1:
            break
        for j in range(1, n+1):
            if st[i][j]:
                pass
            else:
                print("?", i , j)
                stdout.flush()
                x = int(input())
                if x == i:
                    st[j][i] = 1
                    st[i][j] = 1
                    count += 1

            if count >= n-1:
                break
    ans = []
    for i in range(1, n+1):
        for j in range(i, n+1):
            if st[i][j] and i!=j:
                ans.append(i)
                ans.append(j)

    print("!", *ans)
    stdout.flush()

for _ in range(int(input())):
    n = int(input())
    solve(n)
