from itertools import permutations
import re
def validString(string):
    m = re.search(r"^([a-z])(?!\1)([a-z])(?:\1\2)*\1?$", string)
    if m:
        return m.span()[1]
    else:
        return 0
n = input()
s = input()
lengths = [0]
set_s = permutations(set(s), 2)
for i in set_s:
    build = []
    for j in s:
        if j == i[0] or j == i[1]:
            build.append(j)
    lengths.append(validString(''.join(build)))
    
print(max(lengths))
                   
