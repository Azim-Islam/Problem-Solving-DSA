from collections import Counter
for _ in range(int(input())):
    string = input()
    str1 = Counter(string[:len(string)//2])
    str2 = Counter(string[len(string)//2:])

    for k, v in str1.items():
        if k in str2:
            if str1[k] >= str2[k]:
                str2[k] = 0
            else:
                str2[k] = str2[k] - str1[k]
                
    if len(string)%2 == 0:
        print(sum(str2.values()))
    else:
        print(-1)