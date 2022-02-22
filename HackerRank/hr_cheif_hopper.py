from math import ceil

def bruteForceSolution(n, array):
    ans = 0
    val = 1
    for i in range(1, 10**5+1):
        starting = i
        val = i
        for j in array:
            val = val*2 - j
            print(f"arr = {j} val = {val} starting = {starting}")
            if val <= 0:
                break
        if val > 0:
            return starting

n = int(input())
array = map(int, input().split())

print(bruteForceSolution(n, array))