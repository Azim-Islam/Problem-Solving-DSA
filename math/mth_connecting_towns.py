from functools import reduce
def prod(array):
    return reduce(lambda x,y: x*y, array)
for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    result = prod(array)
    print(result%1234567)