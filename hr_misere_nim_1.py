from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt1 = Counter(arr)[1]
    #print(cnt1)
    if cnt1%2==1 and (n-cnt1)%2 == 1:
        print("First")
    else:
        print("Second")
