for _ in range(int(input())):
    n = int(input())
    arr = list(enumerate(list(map(int, input().split()))))
    arr.sort(key=lambda x: x[1])
    print(arr[-1][0]+1)