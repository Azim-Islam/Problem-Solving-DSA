import re
for _ in range(int(input())):
    string = input()
    if re.search("[h].*[a].*[c].*[k].*[e].*[r].*[r].*[a].*[n].*[k]", string):
        print("YES")
    else:
        print("NO")