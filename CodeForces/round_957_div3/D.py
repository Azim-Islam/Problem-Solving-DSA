def solve(arr, n, m, k):
    i = 0
    while i != n+1:
        if arr[i] == 'L':
            f = True
            ii = i
            alt = i
            for j in range(1, m+1):
                if arr[min(i+j, n+1)] == 'L':
                    ii = min(i+j, n+1)
                    f = False
                elif arr[min(i+j, n+1)] == 'W':
                    alt = min(i+j, n+1)
            if f: 
                ii = alt


            if ii == i:
                return False
            else:
                i = ii
        
        elif arr[i] == 'W' and k:
            k -= 1
            i += 1

        elif arr[i] == 'C':
            return False

        elif arr[i] == 'W' and k == 0:
            return False
        

        # print(i, arr[i])
        
    return True


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    arr = ['L'] + list(input())
    arr.append('L')
    if solve(arr, n, m, k):
        print("YES")
    else:
        print("NO")
