import gc
gc.disable()
import sys




input = sys.stdin.readline

    

def solve():
    for _ in range(int(input())):
        n, d, k = map(int, input().split())
        starts = [0]*(n+1)
        ends = [0]*(n+1)
        for __ in range(k):
            l, r = map(int, input().split())
            starts[l] += 1
            ends[r] += 1
            # diff_arr[r+1] -= 1
        
        # print(starts)
        # print(ends)

        bans = 1
        bmax = 0
        ss = 0
        for i in range(1, d+1):
            if starts[i]:
                ss += starts[i]
            # if ends[i]:
                # ss -= ends[i]
        # print(ss)
        bmax = ss
        for i in range(2, n-d+2):
            ss += starts[i+d-1]
            ss -= ends[i-1]
            if ss > bmax:
                bmax = ss
                bans = i
        mans = 1
        bmax = 0
        ss = 0
        for i in range(1, d+1):
            if starts[i]:
                ss += starts[i]
            # if ends[i]:
                # ss -= ends[i]
        # print(ss)
        bmax = ss
        for i in range(2, n-d+2):
            ss += starts[i+d-1]
            ss -= ends[i-1]
            if ss < bmax:
                bmax = ss
                mans = i

        print(bans, mans)

solve()