from collections import defaultdict

input = open('factory.in', 'r').readline
fout = open('factory.out', 'w')

def DFS(node: int, d: defaultdict, visited: list):
    stack: list = []
    stack.append(node)
    while stack:
        for n in d[stack.pop()]:
            stack.append(n)
            visited[n] += 1
        

N = int(input())
d = defaultdict(list)
# We have N nodes, we traverse from each of the nodes (1 to N)
# Lastly we track if such node exists which was visited exactly N-1 times.
# If not then we print -1

for i in range(N-1):
    a, b = map(int, input().split())
    d[a].append(b)

visited = [0]*(N+1)
# DFS would be helpful
for i in range(1, N+1):
    DFS(i, d, visited)

for i in range(1, N+1):
    if visited[i] == N-1:
        print(i, file=fout)
        break
else:
   print('-1', file=fout)