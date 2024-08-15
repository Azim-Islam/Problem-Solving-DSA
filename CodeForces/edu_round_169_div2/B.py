
for _ in range(int(input())):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    count1 = 0

    alice = [0]*102
    bob = [0]*102

    for i in range(a, b+1):
        alice[i] = 1
    
    for i in range(c, d+1):
        bob[i] = 1

    for i in range(1, 101):
        if (alice[i] and bob[i+1]) or (bob[i] and alice[i+1]):
            count1 += 1


    
    print(max(count1, 1))