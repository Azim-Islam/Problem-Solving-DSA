for _ in range(int(input())):
    arr = list(map(int, input().split()))
    for i in range(5):
        arr.sort()
        arr[0] += 1
    print(arr[0]*arr[1]*arr[2])