import sys
from bisect import bisect_right

input = sys.stdin.readline


def compressedIdx(l, ai):
    return bisect_right(l, ai) - 1



def solve():
    updates = []
    queries = []
    indices = set()
    n, q = map(int, input().split())

    for _ in range(n):
        l, r, v = map(int, input().split())
        updates.append([l, r, v])
        indices.add(l)
        indices.add(r)

    for _ in range(q):
        l, r = map(int, input().split())
        queries.append([l, r])
        indices.add(l-1)
        indices.add(r-1)

    indices = sorted(list(indices))

    diff_arr = [0]*(len(indices))

    for l, r, v in updates:
        diff_arr[compressedIdx(indices, l)] += v
        diff_arr[compressedIdx(indices, r)] -= v

    for i in range(1, len(diff_arr)):
        diff_arr[i] = diff_arr[i] + diff_arr[i-1]


    pref_sum = [0]*(len(indices))
    pref_sum[0] = diff_arr[0]

    for i in range(1, len(indices)):
        v = diff_arr[i-1]
        pref_sum[i] = diff_arr[i] + pref_sum[i-1] + v*(indices[i]-indices[i-1]-1)

    pref_sum = [0] + pref_sum

    # print(indices)
    # print(diff_arr)
    # print(list(enumerate(pref_sum)))
    # print(compressedIdx(indices, 2))

    ans = []
    for l, r in queries:
        l = compressedIdx(indices, l-1) + 1
        r = compressedIdx(indices, r-1) + 1
        ans.append(pref_sum[r] - pref_sum[l])


    print("\n".join(map(str, ans)), file=sys.stdout)

solve()