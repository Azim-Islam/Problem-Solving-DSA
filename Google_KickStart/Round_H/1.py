import sys

input = sys.stdin.readline
for t in range(int(input())):
    L, N = map(int, input().split())
    current_d = 0
    after_lapped = 0
    lapped = 0
    previous_lap = 'F'
    count = 0
    for i in range(N):
        d, c = input().strip().split()
        d = int(d)
        
        
        if previous_lap == c or previous_lap == 'F':
            lapped = (after_lapped+d)//L #How many laps
            after_lapped = (after_lapped+d)%L
            count += lapped
            previous_lap = c
        else:
            if after_lapped - d > 0:
                after_lapped -= d
            elif after_lapped - d == 0:
                after_lapped -= d
                previous_lap = c
            elif after_lapped - d < 0:
                lapped = (d - after_lapped)//L #How many laps
                after_lapped = (d - after_lapped)%L
                count += lapped
                previous_lap = c
        # print(previous_lap)
        
    print(f"Case #{t+1}: {count}")