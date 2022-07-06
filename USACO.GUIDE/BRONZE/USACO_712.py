from collections import Counter
read = open('circlecross.in', 'r').readline
write = lambda x : open('circlecross.out', 'w').write(str(x))

s = list(read())
count = 0
for i in range(52):
    for j in range(i+1, 52):
        if s[j] == s[i]:
            count += sum([1 if i == 1 else 0 for i in Counter(s[i+1:j]).values()])
write(count//2)