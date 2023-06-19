for _ in range(int(input())):
    
    arr = list(map(int, input().split()))
    farr = [0]*100
    for i in arr:
        farr[i] += 1
    for i in range(1, 100):
        if farr[i] > farr[i-1]:
            print("NO")
            break
    else:
        print("YES")