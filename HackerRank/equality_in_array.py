from collections import Counter
n = int(input())
count = 0
array = list(map(int, input().split()))
array_dict = dict(Counter(array))
array_dict = list(sorted(array_dict.items(), key = lambda kv:(kv[1], kv[0])))
if len(array_dict) > 1:
    for i in range(len(array_dict)-1):
        count += array_dict[i][1]
    print(count)
else:
    print(count)