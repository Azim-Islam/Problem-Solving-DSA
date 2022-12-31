input = open('cowqueue.in', 'r')
print = lambda x : open('cowqueue.out', 'w').write(str(x)+'\n')


# import sys
# input = sys.stdin

n = int(input.readline())


arr = []
for i in range(n):
  x, y = map(int, input.readline().split())
  arr.append((x, y))
  
arr.sort(key=lambda x: x[0])

time = 0

for k, v in arr:
  time = max(k, time) + v
print(time)