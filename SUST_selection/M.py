a, b = map(int, input().split())
i = 0
t = b
while b > 0:
    b -= 6
    i += 1

if i <= a and t >= a:
    print("Yes")
else:
    print("No")