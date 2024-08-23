from collections import deque


for _ in range(int(input())):
    n, l, r = map(int, input().split())
    arr = deque(map(int, input().split()))
    count = 0
    dd = deque()
    v = 0
    while arr:
        while v < l and arr:
            dd.append(arr.popleft())
            v += dd[-1]
            if l <= v and v <= r:
                count += 1
                v = 0
                dd = deque()

        while v > r:
            v -= dd.popleft()
            if l <= v and v <= r:
                count += 1
                v = 0
                dd = deque()
    
    # if l <= v and v <= r:
    #     count += 1
    #     v = 0
    #     dd = deque()

        
    print(count)

