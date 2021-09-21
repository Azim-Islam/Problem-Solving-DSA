def bin_pow(x, n):
    res = 1
    while n > 0:
        if n&1:
            res = res * x
        x = x*x
        n >>= 1
    return res

def normal_pow(x, n):
    return x**n

print(bin_pow(2, 10**7))
#print(normal_pow(2, 10**7))