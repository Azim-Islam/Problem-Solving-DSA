from collections import Counter

for _ in range(int(input())):
    n = int(input())
    s = list(input())
    c = Counter(s)
    c = [[k, v] for k, v in c.items()]

    c.sort(key=lambda x: x[1], reverse=True)
    # print(c)
    i = 0
    j = len(c) - 1
    new = []
    while i <= j:
        if i <= len(c) - 1:
            new.append(c[i][0])
            c[i][1] -= 1
            if c[i][1] == 0:
                i += 1

        if j >= 0:
            new.append(c[j][0])
            c[j][1] -= 1
            if c[j][1] == 0:
                j -= 1
        # print(i, j)  

    print("".join(new[:n-n%2+1]))