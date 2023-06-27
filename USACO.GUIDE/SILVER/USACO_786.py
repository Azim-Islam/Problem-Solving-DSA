from bisect import bisect_right

input = open('lifeguards.in', 'r').readline
fout = open('lifeguards.out', 'w')


def compIdx(arr, i):
    return bisect_right(arr, i) - 1

def solve():
    n = int(input())
    arr = []
    comp = set()
    comp.add(0)
    max_coverage = 0

    for i in range(n):
        s, e = map(int, input().split())
        comp.add(s+1)
        comp.add(e+1)
        arr.append([s+1, e+1])

    comp = sorted(comp)
    diff_arr = [0]*len(comp)

    for s, e in arr:
        diff_arr[compIdx(comp, s)] += 1
        diff_arr[compIdx(comp, e)] -= 1

    for i in range(1, len(diff_arr)):
        diff_arr[i] = diff_arr[i] + diff_arr[i-1]

    prefix = [0]*(len(diff_arr))
    width = [0]*(len(diff_arr))

    for i in range(len(diff_arr) - 1):
        width[i] = comp[i+1] - comp[i]
        if diff_arr[i] > 0:
            max_coverage += width[i] 
    width[-1] = 1 # needs more analyzing
    if diff_arr[-1]:
        max_coverage += width[-1]
        
    for i in range(1, len(diff_arr)):
        if diff_arr[i] == 1:
            prefix[i] = width[i] + prefix[i-1]
        else:
            prefix[i] = prefix[i-1]

    #need to minus the 0s
    x0 = float('inf')
    u0 = 0

    for s, e in arr:
        s0 = compIdx(comp, s) - 1
        e0 = compIdx(comp, e) - 1
        # u0 += prefix[e0] - prefix[s0]
        x0 = min(x0, prefix[e0]-prefix[s0])

    # print(diff_arr)
    # print(prefix)
    print(max_coverage - x0, file=fout)

solve()