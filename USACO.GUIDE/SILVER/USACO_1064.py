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

for ncow in N_cows:
    for ecow in E_cows:
        if not blocked[ecow.id]:
            #Check which cow gets blocked
            if ecow.x < ncow.x and ncow.y < ecow.y:
                if ncow.x - ecow.x < ecow.y - ncow.y:
                    #East cow blocks the north cow
                    blocked[ncow.id] = 1
                    blames[ecow.id] += blames[ncow.id] + 1
                    break
                elif ncow.x - ecow.x > ecow.y - ncow.y:
                    blocked[ecow.id] = 1
                    blames[ncow.id] += blames[ecow.id] + 1
for i in range(n):
    print(blames[i])