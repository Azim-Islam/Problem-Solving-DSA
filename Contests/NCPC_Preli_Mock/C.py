import sys

input = sys.stdin.readline

def same_sign(a, b):
    if a < 0 and b < 0:
        return True
    elif a >= 0 and b >= 0:
        return True
    else:
        return False

for tt in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    narr = [arr[0]]

    i = 0
    j = 1
    
    while(j < n):
        if same_sign(arr[i], arr[j]):
            j += 1
        else:
            narr.append(arr[j])
            i = j
            j += 1
            
    ans = 0
    if narr[0] <= 0:
        if len(narr)%2 == 1:
            ans = len(narr)//2
        else:
            ans = len(narr)//2 + 1
    else:
        if len(narr)%2 == 1:
            ans = len(narr)//2
        else:
            ans = len(narr)//2 - 1
        
    

    print(f"Case {tt+1}: {sum([i for i in arr if i > 0])} {ans}")
        
        

    