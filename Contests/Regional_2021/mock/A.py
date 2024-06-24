while 1:
    n = int(input())
    if n == 0:
        break
    else:
        if not n%17:    
            print("1")
        else:
            print("0")