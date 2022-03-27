

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    """en_arr = list(enumerate(arr))
    en_arr.sort(key=lambda x: x[1], reverse=True)
    
    prev = float('inf')
    count = 0

    for index, value in en_arr:
        if prev > index:
            prev = index
            count += 1
        else:
            pass
    
    if count%2 == 0:
        print("ANDY")
    else:
        print("BOB")"""
    
    prev = -1
    count = 0
    for i in arr:
        if i > prev:
            count += 1
            prev = i
    if count%2 == 0:
        print("ANDY")
    else:
        print("BOB")