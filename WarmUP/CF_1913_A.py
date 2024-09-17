import gc
gc.disable()
import sys

input = sys.stdin.readline
def solve():
    def check(a, b):
        if a and b  and a[0] != '0' and b[0] != '0':
            if int("".join(a)) < int("".join(b)):
                return 1
        return 0

    for _ in range(int(input())):
        n = list(input().strip())
        for i in range(len(n)):
            if check(n[:i], n[i:]):
                print("".join(n[:i]), "".join(n[i:]), file=sys.stdout)
                break
        else:
            print(-1, file=sys.stdout)

solve()