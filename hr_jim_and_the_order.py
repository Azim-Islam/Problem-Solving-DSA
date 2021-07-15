orders = []
for _ in range(int(input())):
    n = tuple(list(map(int, input().split()))+[_+1])
    orders.append(n)

orders.sort(key=lambda x: (x[0] + x[1], x[0], x[2]))

print(*list(zip(*orders))[2])
