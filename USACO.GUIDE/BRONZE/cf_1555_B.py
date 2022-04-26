for _ in range(int(input())):
    W, H = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    x, y = map(int, input().split())
 
    left_x = x1
    under_y = y1
    right_x = abs(x2-W)
    upper_y = abs(y2-H)
    ans = []
 
    
 
    if under_y+upper_y >= y:
        ans.append(abs(max(under_y, upper_y) - y))
    if left_x + right_x >=x:
        ans.append(abs(max(right_x, left_x) - x))
   
    
 
    if (left_x >= x or right_x >= x or upper_y >= y or under_y >= y):
        ans.append(0)
 
    if len(ans) == 0:
        print(-1)
    else:
        print(f"{min(ans):.9f}")