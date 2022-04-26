print = lambda x : open('speeding.out', 'w').write(str(x)+"\n")


inputs = open('speeding.in', 'r')

N, M = map(int, inputs.readline().split())
"""speed = [0]*101
distance = 1
for _ in range(N):
    seg, max_speed = map(int, inputs.readline().split())
    speed[distance:distance+seg] = [max_speed]*seg
    distance += seg

ans = 0
distance = 0

for _ in range(M):
    seg, max_speed = map(int, inputs.readline().split())
    for i in range(1, seg+1):
        if max_speed > speed[distance+i]:
            ans = max(max_speed - speed[distance+i], ans)
    distance += seg 
print(ans)
"""
#Alternative solution
speed_limits = []
distance = 1
for _ in range(N):
    seg, max_speed = map(int, inputs.readline().split())
    start = distance
    end = distance + seg - 1
    speed_limits.append((start, end, max_speed))
    distance += seg

distance = 1
ans = [0]
for _ in range(M):
    seg, max_speed = map(int, inputs.readline().split())
    start = distance
    end = distance + seg - 1
    for i in speed_limits:
        if (i[0] <= start <= i[1]) or (i[0] <= end <= i[1]):
            ans.append(max_speed-i[2])
    distance += seg

print(max(ans))