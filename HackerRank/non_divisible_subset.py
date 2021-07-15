from collections import Counter
n, k = map(int, input().split())
array_n = (list(map(int, input().split())))
array_mods = [i%k for i in array_n]
counts = 0
counted = Counter(array_mods)
for mod, count in counted.items():
    if (count*mod) % k == mod:
        counted[mod] = 1
counted = {i:j for i,j in sorted(counted.items(), key = lambda x : x[1], reverse=True)}
black_list = set()
for mod,count in counted.items():
    if mod not in black_list:        
        for i in counted.keys():
            if (mod + i) % k == 0:
                black_list.add(i)
                break
        counts += count
print(counts)
#print(counted)
