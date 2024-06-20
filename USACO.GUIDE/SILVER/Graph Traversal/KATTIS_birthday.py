from collections import defaultdict


class Edge:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def check(e, node, nn):
    node, nn = min(node, nn), max(node, nn)
    e.x, e.y = min(e.x, e.y), max(e.x, e.y)
    if e.x == node and nn == e.y:
        return False
    return True

while True:
    p, c = map(int, input().split())
    if not (p == 0 and c==0):
        adj = [[0]*101 for _ in range(101)]
        edges = []
        for _ in range(c):
            a, b = map(int, input().split())
            adj[a][b] = 1
            adj[b][a] = 1

            edges.append(Edge(a, b))

        f = False
            
        for e in edges:
            #DFS
            stack = [0]
            c = 0
            visited = [0]*(p+1)
            while stack:
                node = stack.pop()
                for nn in range(0, 101):
                    if (adj[node][nn] or adj[nn][node])and not visited[nn] and check(e, node, nn):
                        stack.append(nn)
                        c += 1
                        visited[nn] = 1
            if c != p:
                f = True
                break

        if f:
            print("Yes")
        else:
            print('No')
    else:
        break