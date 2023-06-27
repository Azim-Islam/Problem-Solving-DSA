from itertools import permutations
from string import ascii_lowercase
import random

import sys
input = sys.stdin.readline


class myString():
    def __init__(self, s) -> None:
        self.s = s

    def __lt__(self, other):
        s1 = self.s
        s2 = other.s

        s3 = s1+s2
        s4 = s2+s1
        if s3 < s4:
            return True
        else:
            return False

        
    def __repr__(self) -> str:
        return self.s
    def __str__(self) -> str:
        return self.s


arr = []
for i in range(int(input())):
    l = input().strip()
    arr.append(myString(l))
arr.sort()
print("".join(map(str, arr)))

# while True:
#     inputs = []
#     for i in range(random.randint(1, 3)):
#         inputs.append("".join(random.choices(ascii_lowercase, k=random.randint(1,50))))
#     arr = []
#     arr1 = []
#     for i in range(len(inputs)):
#       l = inputs[i]
#       arr.append(myString(l))
#       arr1.append(l)
#     arr.sort()

#     ans = ["".join(i) for i in permutations(arr1)]

#     if "".join(map(str, arr)) != min(ans):
#         print(inputs)
#         print("".join(map(str, arr)))
#         print(min(ans))
#         break