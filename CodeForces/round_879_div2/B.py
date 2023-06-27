for _ in range(int(input())):
    L, R = input().split()
    L = ['0']*(101-len(L)) + list(L)
    R = ['0']*(101-len(R)) + list(R)
    idx = 101
    for i in range(0, 101):
        if L[i] == R[i]:
            idx = i
        else:
            break
    L = L[idx+1:]
    R = R[idx+1:]
    ans = 0
    # print(L, R)
    try:
        ans += abs(int(L[0])-int(R[0]))
    except:
        pass
    for i in range(1, len(L)):
        ans += abs(9-0)
        # else:
        #     
    print(ans)