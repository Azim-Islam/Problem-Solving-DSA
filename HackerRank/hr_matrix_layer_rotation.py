m, n, r = map(int, input().split())

matrix = []

for _ in range(m):
    matrix.append(list(map(int, input().split())))


def rotateMatrix(matrix):
    rotatedMatrix = [[0 for i in range(n)] for j in range (m)]
