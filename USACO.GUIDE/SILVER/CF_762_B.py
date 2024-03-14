import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
m = int(input())

usb = []
ps = []

for _ in range(m):
    v, k = input().split()
    if k == "USB":
        usb.append(int(v))
    else:
        ps.append(int(v))

usb.sort()
ps.sort()

cost = 0
computers = 0

# for _ in range(a):
#     if usb:
#         v = usb.pop()
#         cost += v
#         computers += 1

computers += min(len(usb), a)
cost += sum(usb[0:min(len(usb), a)])
usb = usb[min(len(usb), a):]

# for _ in range(b):
#     if ps:
#         v = ps.pop()
#         cost += v
#         computers += 1

computers += min(len(ps), b)
cost += sum(ps[0:min(len(ps), b)])
ps = ps[min(len(ps), b):]


aa = usb+ps
aa.sort()

# for _ in range(c):
#     if aa:
#         v = aa.pop()
#         cost += v
#         computers += 1
computers += min(len(aa), c)
cost += sum(aa[0:min(len(aa), c)])

print(computers, cost)