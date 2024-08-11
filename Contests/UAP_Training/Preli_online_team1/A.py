for _ in range(int(input())):
    n, r = map(int, input().split())
    arr = map(int, input().split())
    if sum(arr)+1500 == r:
        print("Correct")
    else:
        print("Bug")