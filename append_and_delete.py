s = (input())
t = (input())
k = int(input())
pi = 0
answer = 0
while pi<=len(s):
    pi += 1
    if s[0:pi] == t[0:pi]:
        continue
    else:
        break
pi -= 1
temp = len(t)+pi
answer = len(s)+len(t) - pi*2
print(answer)
if answer <= k and ((len(t)+len(s))%2 == k%2) or len(s)+len(t) < k:
    print('Yes')

else:
    print('No')