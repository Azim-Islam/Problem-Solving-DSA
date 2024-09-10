for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[0]*arr[2])