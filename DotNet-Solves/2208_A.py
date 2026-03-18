from collections import defaultdict

for _ in range(int(input())):
    n, k, p, m = map(int, input().split())
    arr_i = list(map(int, input().split()))
    d_dict = defaultdict(int)
    # build the dictionary
    for i, v in enumerate(arr_i):
        d_dict[i+1] = v
        
    ans = 0
    flag = 0
    
    while m >= 0:
        # print(d_dict)
        flag = 0
        for i, (card, cost) in enumerate(d_dict.items()):
            if i >= k: 
                break
            if card == p and m - cost >= 0:
                ans += 1
                m -= cost
                d_dict.pop(card)
                flag = 1
                d_dict[card] = cost
                break
        if not flag:    
            maxx = [0, float('inf')]
            for i, (card, cost) in enumerate(d_dict.items()):
                if i >= k: 
                    break
                if maxx[1] > cost:
                    maxx = [card, cost]
            if maxx[1] <= m:
                m -= maxx[1]
                d_dict.pop(maxx[0])
                d_dict[maxx[0]] = maxx[1]
            else:
                break
    print(ans)