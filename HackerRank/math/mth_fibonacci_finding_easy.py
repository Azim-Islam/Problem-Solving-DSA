from math import sqrt

A = [ 1, 1, 1, 0]
mod = 10**9+7
def matrix_multiply(A, B):
    if len(B) > 2:
        return [
            A[0]*B[0]%mod + A[1]*B[2]%mod, A[0]*B[1]%mod + A[1]*B[3]%mod,
            A[2]*B[0]%mod + A[3]*B[2]%mod, A[2]*B[1]%mod + A[3]*B[3]%mod
        ]
    else:
        return [
            A[0]*B[0]%mod + A[1]*B[1]%mod,
            A[2]*B[0]%mod + A[3]*B[0]%mod
        ]
        
    
def matrix_pow(A, n):
    n -= 1
    res = A
    while n > 0:
        if n&1:
            res = matrix_multiply(res, A)
        A = matrix_multiply(A, A)
        n >>= 1
    return res
    
    
    
A = [1,1,1,0]
for i in range(int(input())):
    X, Y, N = map(int, input().split())
    if N == 0:
        print(X)
    elif N == 1:
        print(Y)
    else:
        print(matrix_multiply(matrix_pow(A, N-1), [Y, X])[0]%mod)