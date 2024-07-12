
def solve(n):
    pairs = []
    nn = int("".join(str(n)*9))
    # print(nn)
    l = len(str(n))
    while nn:
        ll = len(str(nn))
        for i in range(1, 10_000):
            if (nn+i)%n == 0:
                a = (nn+i)//n
                if ll == (a*l-i):
                    pairs.append([a, i])
        nn = nn//10

    print(len(pairs))
    for a, b in pairs:
        print(a, b)


for _ in range(int(input())):
    n = int(input())
    solve(n)