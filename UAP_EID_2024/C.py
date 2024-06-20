from operator import truediv


def left_right(m, n, k):
    ans = []
    for i in range(1, n+1):
        c = i//2+(i%2)
        t = 0
        for j in range(1, c+1):
            y = j
            x = (i-j)+1
            # print(x, y)
            # print(y, x)

            y -= 1
            x -= 1
            if m[x][y] == "@":
                t += 1
            if m[y][x] == "@" and x != y:
                t += 1

            
        # print('='*10)
        ans.append(t)
    for i in range(n):
        m[i] = m[i][::-1]
    m = m[::-1]

    for i in range(1, n):
        c = i//2+(i%2)
        t = 0
        for j in range(1, c+1):
            y = j
            x = (i-j)+1
            # print(x, y)
            # print(y, x)

            y -= 1
            x -= 1
            if m[x][y] == "@":
                t += 1
            if m[y][x] == "@" and x != y:
                t += 1

            
        # print('='*10)
        ans.append(t)

    ans.sort(reverse=True)
    for i in range(n):
        m[i] = m[i][::-1]
    m = m[::-1]
    return sum(ans[:k])

def top_down(m, n, k):
    ans = []
    for i in range(n):
        t = 0
        for j in range(n):
            if m[j][i] == '@':
                t += 1
        ans.append(t)
    ans.sort(reverse=True)
    return sum(ans[:k])

    

n, k = map(int, input().split())
m = []

for _ in range(n):
    m.append(list(input()))

    

print(max(left_right(m, n, k), left_right(m, n, k), top_down(m, n, k)))


