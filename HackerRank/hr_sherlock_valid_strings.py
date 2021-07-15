from collections import Counter
string = input()
counted = Counter(string)
v_freq = [(k,v) for k,v in sorted(Counter(counted.values()).items(), key = lambda x: x[1], reverse = True)]
# print(v_freq)
if  len(v_freq) == 1:
    print("YES")        
elif len(v_freq) > 2:
    print("NO")
else:
    if abs(v_freq[1][0]-v_freq[0][0]) == 1 and v_freq[-1][1] == 1 or (v_freq[-1][1] == 1 and v_freq[-1][0] == 1):
        print("YES")
    else:
        print("NO")
