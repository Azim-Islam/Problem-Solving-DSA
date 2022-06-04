
inputs = open('traffic.in', 'r')
print = lambda x : open('traffic.out', 'w').write(str(x)+'\n')

 

def sol(INS):
    ans = find_first(INS)
    ans += "\n"+find_last(INS)
    print(ans)

def find_first(INS):
    n_p = []
    for status, lower, upper in INS[::-1]:
        if status == "none":
            if len(n_p) == 0:
                n_p.append(lower)
                n_p.append(upper)
            n_p[0] = max(n_p[0], lower)
            n_p[1] = min(n_p[1], upper)
        if status == "on" and len(n_p) > 0:
            n_p[0] -= upper # May have error
            n_p[1] -= lower #
            n_p[0] = max(0, n_p[0])
            n_p[1] = max(0, n_p[1])
        elif status == "off" and len(n_p) > 0:
            n_p[0] += lower
            n_p[1] += upper
    return f"{n_p[0]} {n_p[1]}"

def find_last(INS):
    n_p = []
    for status, lower, upper in INS:
        if status == "none":
            if len(n_p) == 0:
                n_p.append(lower)
                n_p.append(upper)
            n_p[0] = max(n_p[0], lower)
            n_p[1] = min(n_p[1], upper)
        elif status == "off" and len(n_p) > 0:
            n_p[0] -= upper
            n_p[1] -= lower
            n_p[0] = max(0, n_p[0])
            n_p[1] = max(0, n_p[1])

        elif status == "on" and len(n_p) > 0:
            n_p[0] += lower
            n_p[1] += upper
    return f"{n_p[0]} {n_p[1]}"

# def find_first(INS):


N = int(inputs.readline())


INS = []
for line in inputs.readlines():
    status, lower, upper = line.split()
    lower = int(lower)
    upper = int(upper)
    INS.append([status, lower, upper])

sol(INS)