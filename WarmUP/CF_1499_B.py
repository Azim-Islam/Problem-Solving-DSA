from string import printable


for _ in range(int(input())):
    s = list(map(int, list(input())))
    ONE_F = True
    ZERO_F = False
    last_one = 0
    last_zero = 0
    for i in range(0, len(s)-1):
        if s[i] == s[i+1] and s[i] == 1:
            last_one = i+1
            break
        
    for i in range(last_one, len(s)-1):
        if s[i] == s[i+1] and s[i] == 0:
            last_zero = i+1
            break
    
    if last_one and last_zero:
        print("NO")
    else:
        print("YES")