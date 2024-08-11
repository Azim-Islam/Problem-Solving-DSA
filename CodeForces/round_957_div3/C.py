for _ in range(int(input())):
    n, m, k = map(int, input().split())
    big_arr = []
    small_arr = []
    middle_arr = []

    for i in range(n, k-1, -1):
        big_arr.append(i)

    for i in range(1, m+1):
        small_arr.append(i)

    for i in range(k-1, m, -1):
        middle_arr.append(i)
    
    middle_arr = middle_arr[::-1]

    print(*big_arr+middle_arr+small_arr)