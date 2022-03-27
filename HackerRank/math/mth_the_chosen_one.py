from cmath import inf
from math import sqrt



n = int(input())
arr = list(map(int, input().split()))

def find_mins(arr):
    lowest = float('inf')
    snd_lowest = float('inf')
    for i in range(len(arr)):
        if arr[i] < lowest:
            snd_lowest = lowest
            lowest = arr[i]
        elif arr[i] < snd_lowest:
            snd_lowest = arr[i]

    return (lowest, snd_lowest)
        


def find_factors(n):
    factors = []
    for i in range(1, int(sqrt(n))+1):
        if n%i == 0:
            factors.append(i)
            factors.append(n//i)
    return set(factors)

if n > 1:
    lowest, snd_lowest = find_mins(arr)
    total_factors = find_factors(lowest).union(find_factors(snd_lowest))

    for i in total_factors:
        count = 0
        for j in arr:
            if j%i == 0:
                count += 1
        if count == n-1:
            print(i)
            break
else:
    print(arr[0]+1)