n, k = map(int, input().split())
arr_k = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

from functools import reduce

all_probs = []

for i in arr_b:
    t_set = set()
    x = 0
    for j in arr_k:
        x += j
        t_set.add(i-x)
    all_probs.append(t_set)

final_set = reduce(lambda x,y: x.intersection(y), all_probs)
print(len(final_set))