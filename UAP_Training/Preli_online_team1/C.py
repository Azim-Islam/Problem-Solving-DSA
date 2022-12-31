for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    f = True
    k = 0
    for i in range(n):
        if b[i] == '0' and a[i] == '1':
            print("IMPOSSIBLE")
            f = False
            break
        if b[i] == '1' and a[i] == '1':
            k += 1
    if f:
        print(pow(2, k, 1000000007))