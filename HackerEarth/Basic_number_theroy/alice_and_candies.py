#https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/practice-problems/algorithm/lola-and-candies-36b57b1b/
from math import sqrt
n = int(input())

sqrt = sqrt

# x_1 = lambda a, s, d: (-(2*a - d) + sqrt((2*a-d)**2 + 8*s*d))/(2*d)
# # x_2 = lambda a, s, d: (-(2*a - d) - sqrt((2*a-d)**2 + 8*s*d))/(2*d)


# s = n
# d = 2

# count = 0

# sr = 0 
# for i in range(1, n//2+1, 2):
#     v = x_1(i, s, d)
#     s0 = (v*(2*i + (v-1)*d))/2
#     if s0 == s and int(v) == v:
#         print(i, v)
#         count += 1
#         sr = i
# print(i, n/i)

# if n%2: count += 1
# print(count)

x_1 = lambda i, s, d: (2*s - i*d*(i-1))/(2*i)
count = 0
s = n
d = 2

for i in range(1, 10**5+1):
    a = x_1(i, s, d)
    if int(a) == a and a%2 == 1:
        if a < 0:
            break
        count += 1
print(count)


