from collections import defaultdict
d_count = defaultdict(int)
int_strings = int(input())
int_gems = 0
for _ in range(int_strings):
    string = set(input())
    for i in string:
        d_count[i] += 1
for i,j in d_count.items():
    if j == int_strings:
        int_gems += 1
print(int_gems)