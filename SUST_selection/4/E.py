
import sys 
sys.setrecursionlimit(10**7)

t = int(input())
girls = set(['a', 'b', 'c'])

def iv(i, j, maze, m, n, visited):
    if 0 <= i <= m and 0 <= j <= n and (maze[i][j] == "." or maze[i][j] == "h"):
        return True
    else: 
        return False





for x in range(t):
    m, n = list(map(int, input().split()))
    maze = []
    dic = {'a': float('inf'), 'b': float('inf'), 'c':float('inf')}
    for i in range(m):
        maze.append(input())
    ans = 0
    for i in range(m):
        for j in range(n):
            if maze[i][j] in girls:
                a, b = i, j
                visited = [[float('inf')]*n for _ in range(m)]
                stack = [(i, j, 0)]
                visited[i][j] = 0
                while stack:
                    # print(stack)
                    # print(visited)
                    v = stack.pop()
                    a, b = v[0], v[1]
                    
                    if maze[a][b] == 'h':
                        dic[maze[i][j]] = min(visited[a][b], dic[maze[i][j]])
                        
                    else:
                        # print(iv(a+1, b, maze, m, n, visited))
                        # print(iv(a-1, b, maze, m, n, visited))
                        # print(iv(a, b+1, maze, m, n, visited))
                        # print(iv(a, b-1, maze, m, n, visited))

                        if iv(a+1, b, maze, m, n, visited) and v[2]+1 < visited[a+1][b]:
                            stack.append((a+1, b, v[2]+1))
                            visited[a+1][b] = v[2]+1

                        if iv(a-1, b, maze, m, n, visited) and v[2]+1 < visited[a-1][b]:
                            stack.append((a-1, b, v[2]+1))
                            visited[a-1][b] = v[2]+1
        
                        if iv(a, b+1, maze, m, n, visited) and v[2]+1 < visited[a][b+1]:
                            stack.append((a, b+1, v[2]+1))
                            visited[a][b+1] = v[2]+1

                        if iv(a, b-1, maze, m, n, visited) and v[2]+1 < visited[a][b-1]:
                            stack.append((a, b-1, v[2]+1))
                            visited[a][b-1] = v[2]+1
                

    print(f"Case {x+1}: {max(dic.values())}")