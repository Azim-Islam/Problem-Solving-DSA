from math import ceil, log


for _ in range(int(input())):
    N, K = map(int, input().split()) #N = numbers of ai # K = sum
    if N == 1 or K == 1:
        print(K, "0 "*(N-1))
    else:
        first = 2 ** ceil(log(K, 2) - 1) - 1
        print(first, K - first, "0 "*(N-2))