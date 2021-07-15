'''This one kicked my butt. Python 3 solution:

def nonDivisibleSubset(k, s):
    r, o = [0] * k, 0                            # 1
    for i in s:
        r[i % k] += 1                            # 2
    for j in range((k + 2) // 2):                # 3
        if not j or not k % 2 and j == k // 2:
            o += r[j] > 0                        # 4
        else:
            o += max(r[j], r[k - j])             # 5
    return(o)

Relying on the observation that a // k + b // k and (a + b) // k are equivalent...

   1 We declare a bucket for remainders and a counter for the largest subset size.
   2 We iterate through s, dividing each element i by k to calculate a remainder. We increment the value of the bucket at the index of the remainder.
   3 We next iterate half way through the bucket to avoid over-counting.
   4 If the value of the bucket is greater than 0 at index 0 or index k // 2 where k is even, we increment the counter by 1.
   5 Otherwise, we increment the counter by the value of the bucker at index j or k - j, whichever is greater.
'''
n, k = map(int, input().split())
array_n = set(map(int, input().split()))
count = 0
array_mods = [0]*k
for i in array_n:
    array_mods[i%k] += 1
#print(array_mods)
for j in range((k//2 +1)):
    if (j==0) or ((k%2 == 0) and (j == k//2)):
    #if not j or not k % 2 and j == k // 2:
        count += array_mods[j] > 0
    else:
        count += max(array_mods[j], array_mods[k-j])
        #print(max(array_mods[j], array_mods[k-j]))
print(count)
print(list(enumerate(array_mods)))