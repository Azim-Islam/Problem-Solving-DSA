from collections import deque
import sys

def pp(s):
    print("?", "".join(map(str, s)))
    sys.stdout.flush()
    return int(input())

for _ in range(int(input())):
    n = int(input())
    queries = 0
    s = deque([0])
    if not pp(s):
        s.pop()
        s.append(1)

    left_closed = False

    while True:
        if len(s) == n or left_closed:
            break
        if not left_closed:
            s.appendleft(s[0]^1)
            if not pp(s):
                s[0] = s[0]^1
                if not pp(s):
                    s.popleft()
                    left_closed = True

    while True:
        if len(s) == n:
            break
        if len(s) == n-1:
            s.append(s[-1]^1)
            if not pp(s):
                s[-1] = s[-1]^1
            break

        else:
            s.append(s[-1]^1)
            if not pp(s):
                s[-1] = s[-1]^1

    print("!", "".join(map(str, s)))
    sys.stdout.flush()
