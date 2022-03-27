for _ in range(int(input())):
    n = int(input())
    arr = input()
    enum_arr = enumerate(arr)
    ans = 0
    for index, value in enum_arr:
        if value == "0" and index + 1 < n:
            try:
                if arr[index+1] == "1" and arr[index+2] == "0":
                    ans += 1
                elif arr[index+1] == "0":
                    ans += 2
            except:
                if arr[index+1] == "0":
                    ans += 2
           
    print(ans)