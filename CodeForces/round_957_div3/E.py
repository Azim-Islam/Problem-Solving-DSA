

def ff(dig, i, n):
    dig = list(str(dig))
    n = list(str(n))
    dig.extend(n[0:i%len(n)])
    print(dig)
    return int("".join(dig))


def find_pairs(dig, n):
    pairs = []
    for b in range(1, 10_000+1):
        if (dig+b)%n == 0:
            pairs.append([(dig+b)//n, b])
    # print(pairs)
    return pairs

def solve(n):
    pairs = []
    dig = n
    i = 1
    while dig <= 10_000:
        dig = ff(dig, i, n)
        print(dig)
        pairs.extend(find_pairs(dig, n))
        i += 1
    
    print(len(pairs))
    for a, b in pairs:
        print(a, b)


for _ in range(int(input())):
    n = int(input())
    solve(n)