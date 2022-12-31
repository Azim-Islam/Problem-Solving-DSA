n = int(input())
arr = list(map(int, input().split()))


odd, even = 0, 0

for i in arr:
    if i%2:
        odd += 1
    else:
        even += 1

groups = max(max(0, 2*min(even-1, odd) + 1), 2*min(even, odd))
r = odd - min(even, odd)

#Last one in ODD!
t = r
for i in range(r):
    if i%2 == 0:
        if t-2 >= 0:
            groups += 1
            t -= 2
        else:
            break
    else:
        if t-1 >= 0:
            groups += 1
            t -= 1
        else:
            break
if t > 0:
    groups -= 1

print(groups)

n = int(input())
breedID = list(map(int,input().split()))

odd = even = 0
for i in range(n):
    if breedID[i]%2:
        odd += 1
    else:
        even += 1

result = 0

temp = min(odd, even)
result += temp*2

odd -= temp
even -= temp

if not odd and even:
    result+=1
else:
    result += (odd//3)*2
    odd %= 3
    result += odd//2
    odd %= 2
    result -= odd

print(result)
