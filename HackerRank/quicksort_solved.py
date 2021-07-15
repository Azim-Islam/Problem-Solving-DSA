def quick_sort(*ar):
    p, *a = ar
    first, last = [], []
    for i in a:
        if i < p:
            first.append(i)
        else:
            last.append(i)
    if len(first) > 1:
        first = quick_sort(*first)
        print(*first)
    if len(last) > 1:
        last = quick_sort(*last)
        print(*last)
    return first + [p] + last

n = int(input())
p, *a = map(int, input().split())
print(*quick_sort(p, *a))