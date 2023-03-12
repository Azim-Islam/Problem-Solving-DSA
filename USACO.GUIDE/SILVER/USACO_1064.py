class cow:
    def __init__(self, id, direction, x, y) -> None:
        self.d = direction
        self.id = id
        self.x = int(x)
        self.y = int(y)

n = int(input())

N_cows = []
E_cows = []
blames = [0]*n
blocked = [0]*n
for i in range(n):
    d, x, y = input().split()
    if d == 'N':
        N_cows.append(cow(i, d, x, y))
    else:
        E_cows.append(cow(i, d, x, y))

N_cows.sort(key=lambda cow: cow.x)
E_cows.sort(key=lambda cow: cow.y)
