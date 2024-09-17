import gc


gc.disable()

def rr(a, b):
    c = float('inf')
    n = len(a)
    for i in range(0, len(b)-n+1):
        if a == b[i:i+n]:
            # c = min(c, i + (len(b) - (i+n)))
            c = min(c, len(b)-n)

    #         print(a, b, i + (len(b) - (i+n)))
    # # print(c)
    return c 

def check(a, b):
    if a == b:
        return 0
    ans = float('inf')
    for i in range(0, len(a)):
        for j in range(0, len(a)-i+1):
            # print(a[j:j+i])
            v = rr(a[j:j+i], b)
            # print(a[j:j+i], v)
            # vv = v + j + (len(a) - (j+i))
            vv = v + len(a) - (i)
            ans = min(ans, vv)
            # print(vv)
    return ans

for _ in range(int(input())):
    a = input()
    b = input()
    v =min(check(a, b), check(b, a))
    print(v)