# Basic matrix multiplication program
from sys import stdin


def readint():
    return int(stdin.readline())


def readarray():
    return list(map(int, stdin.readline().split()))


def readmatrix(n):
    M = []
    for _ in range(n):
        M.append(readarray())
    return M

def mulmatrix(M, V):
    #result = [[0]*len(V[0])]*len(M)
    result = [[0 for i in range(len(V[0]))] for j in range(len(M))]
    print(result)
    for i in range(len(M)):
        for j in range(len(V[0])):
            mul = 0

            for k in range(len(V)):
                mul += M[i][k]*V[k][j]
            result[i][j] = mul
            print(result)
    return result

if __name__ == "__main__":
    print("Matrix A rows")
    n = readint()
    print("Enter Matrix A")
    M = readmatrix(n)
    print("Matrix B rows")
    m = readint()
    print("Enter Matrix B")
    V = readmatrix(m)


    print(M)
    print(V)

    print(mulmatrix(V, M))
