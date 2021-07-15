import re
string = input()
#re_pat = r"([a-zA-Z0-9])+"
m = re.search(r"([a-zA-Z0-9])\1", string)
if m:
    print(m.group(0)[0])
else:
    print("-1")