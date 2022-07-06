import sys
from collections import defaultdict
read = sys.stdin.readline
# write = sys.stdin.writelines


# x = lambda i, x: 1 if x[0] == "G" and i < x[1] else 0
# y = lambda i, x: 1 if x[0] == "L" and i > x[1] else 0
a = {"G": lambda i, x: 1 if i < x else 0,
 "L": lambda i, x: 1 if i > x else 0}

def solve(arr, set_a):
    min_count = float('inf')
    for i in set_a:
        count = 0
        for j in range(len(arr)):
            count += a[arr[j][0]](i, arr[j][1])
        min_count = min(min_count, count)
    print(min_count)

def main():
    arr = []
    set_a = set()
    for i in range(int(read())):
        p, v = read().split()
        v = int(v)
        set_a.add(v)
        arr.append((p, v))
    solve(arr, set_a)
main()


