inputs = open('tttt.in', 'r')
print = lambda x : open('tttt.out', 'w').write(str(x)+'\n')

board = []
for _ in range(3):
    board.append(list(inputs.readline()))


import copy
from itertools import combinations
from string import ascii_uppercase

def find_wins(tmp_board, i, j):
    for k in tmp_board:
        if k.count(i) == 3 or k.count(j) == 3:
            return 1
    tmp_list = []
    for a in range(3):
        list_a = [0]*3
        for b in range(3):
            list_a[b] = board[b][a]
        tmp_list.append(list_a)
    for k in tmp_list:
        if k.count(i) == 3 or k.count(j) == 3:
            return 1

    diag1 = [tmp_board[0][0], tmp_board[1][1], tmp_board[2][2]]
    diag2 = [tmp_board[0][2], tmp_board[1][1], tmp_board[2][0]]
    if diag1.count(i) == 3 or diag2.count(i) == 3:
        return 1
    if diag1.count(j) == 3 or diag2.count(j) == 3:
        return 1
    return 0

def find_wins1(tmp_board, i, j):
    wins = 0
    for k in tmp_board:
        i_ = k.count(i)
        j_ = k.count(j)
        if i_ + j_ == 3 and i_ > 0 and j_ > 0:
            return 1
    tmp_list = []
    for a in range(3):
        list_a = [0]*3
        for b in range(3):
            list_a[b] = board[b][a]
        tmp_list.append(list_a)
    for k in tmp_list:
        i_ = k.count(i)
        j_ = k.count(j)
        if i_ + j_ == 3 and i_ > 0 and j_ > 0:
            return 1

    k = [tmp_board[0][0], tmp_board[1][1], tmp_board[2][2]]
    i_ = k.count(i)
    j_ = k.count(j) 78 lines (66 sloc) 1.93 KB

    if i_ + j_ == 3 and i_ > 0 and j_ > 0:
        return 1
    k = [tmp_board[0][2], tmp_board[1][1], tmp_board[2][0]]
    i_ = k.count(i)
    j_ = k.count(j)
    if i_ + j_ == 3 and i_ > 0 and j_ > 0:
        return 1
    return 0


single_wins = 0
for i in ascii_uppercase:
    single_wins += find_wins(board, i, i)
ans = str(single_wins)

team_wins = 0
for i,j in list(combinations(ascii_uppercase, 2)):
    team_wins += find_wins1(board, i, j)
    

ans += "\n"+str(team_wins)
print(ans)



#solution with set
input = open('tttt.in', 'r').readline
print = lambda x : open('tttt.out', 'w').write(str(x)+'\n')




from collections import defaultdict


arr = []

for i in range(3):
    arr.append(input().rstrip())

# rows
r = defaultdict(set)
for i in range(3):
    for j in range(3):
        r[i].add(arr[i][j])

# columns
c = defaultdict(set)
for i in range(3):
    for j in range(3):
        c[i].add(arr[j][i])

# diagonals
d = defaultdict(set)
d[1].add(arr[0][0])
d[1].add(arr[1][1])
d[1].add(arr[2][2])

d[2].add(arr[0][2])
d[2].add(arr[1][1])
d[2].add(arr[2][0])


def sol(r, c, d, x):
    wins1 = set()
    for k in r:
        if len(r[k]) == x:
            wins1.add("".join(sorted(r[k])))
    for k in c:
        if len(c[k]) == x:
            wins1.add("".join(sorted(c[k])))
    for k in d:
        if len(d[k]) == x:
            wins1.add("".join(sorted(d[k])))
    return len(wins1)


# single wins
a1 = sol(r, c, d, x=1)
# dual wins
a2 = sol(r, c, d, x=2)

print(str(a1) +'\n' + str(a2))
