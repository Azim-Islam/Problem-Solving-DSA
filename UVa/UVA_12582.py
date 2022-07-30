from string import ascii_uppercase
from collections import defaultdict

for t in range(int(input())):
    arr = list(input())
    stack = []
    ans_dict = defaultdict(int)
    stack.append(arr[0])
    for i in arr[1:]:
        if i == stack[-1] and len(stack) > 1:
            v = stack.pop()
            ans_dict[v] += 1
            ans_dict[stack[-1]] += 1
        else:
            stack.append(i)
    print("Case {}".format(t+1))
    print("\n".join(["{} = {}".format(i, ans_dict[i]) for i in ascii_uppercase if i in ans_dict]))