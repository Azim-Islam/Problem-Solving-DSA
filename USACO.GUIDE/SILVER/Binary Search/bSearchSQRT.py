

def binary_sqrt(x):
    lo = 0
    hi = x

    for _ in range(1111//2+50):
        mid = (lo + hi)/2
        print(f"{_} :-> {mid:.100}")
        if mid*mid <= x:
            lo = mid
        else:
            hi = mid
    
    return lo


binary_sqrt(10)