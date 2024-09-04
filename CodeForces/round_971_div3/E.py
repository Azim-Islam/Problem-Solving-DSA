def f(lo, n, k):
    aa = ssum(lo)+k*lo
    bb = ssum(n)+k*(n) - aa
    return abs(aa-bb)

def check(mid, n, k):
    aa = ssum(mid)+k*mid
    bb = ssum(n)+k*(n) - aa
    if aa <= bb:
        return True
    else:
        return False

def ssum(n):
    n -= 1
    return (n*(n+1))//2

for _ in range(int(input())):
    n, k = map(int, input().split())
    lo = 0
    hi = n
    while hi - lo > 1:
        mid = (hi+lo)//2
        if check(mid, n, k):
            lo = mid
        else:
            hi = mid 

    # lo += 1
    # print(lo)
    aa = ssum(lo)+k*lo
    bb = ssum(n)+k*(n) - aa
    print(min(f(lo, n, k), f(lo+1, n, k)))
    # print(lo, aa, bb, abs(aa-bb))
    # a1 = abs(aa-bb)

    # lo += 1
    # aa = ssum(lo)+k*lo
    # bb = ssum(n)+k*(n-lo) - aa
    # # print(abs(aa-bb))
    # a2 = abs(aa-bb)
    # print(min(a1, a2))
