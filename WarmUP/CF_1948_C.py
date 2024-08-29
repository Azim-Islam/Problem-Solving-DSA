

for _ in range(int(input())):
    n = int(input())
    m = []
    m.append(list(input()))
    m.append(list(input()))
    # dp = [[0]*n, [0]*n]
    stack = []
    stack.append((1, n-1))
    visited = set()
    visited.add((1, n-1))
    f = True
    
    while stack:
        i, j = stack.pop()

        if i == 0 and j == 0:
            f = False
            print("YES")
            break
            
        if j-1 >= 0 and m[i][j-1] == ">":
            i, j = i, j-1
            next_i, next_j = (0 if i == 1 else 1, j)
            if (next_i, next_j) not in visited:
                stack.append((next_i, next_j))
                visited.add((next_i, next_j))
            if j-1 >= 0 and (i, j-1) not in visited:
                stack.append((i, j-1))
                visited.add((i, j-1))
    
    if f:
        print("NO")
