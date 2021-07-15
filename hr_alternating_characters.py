from itertools import groupby
for _ in range(int(input())):
    string = input()
    count = 0
    for k,g in groupby(string):
        count += len(list(g))-1
    print(count)