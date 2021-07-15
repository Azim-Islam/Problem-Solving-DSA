for _ in range(int(input())):
    n = int(input())
    count = 0
    array = list(map(int, input().split()))

    for j in range(n, 1, -1):
        for i in range(j-1, 0, -1):
            if array[j-1]*array[i-1] == i+j:
                print(i+1, j+1, array[j-1]*array[i-1])
                count += 1
                
    print(count)