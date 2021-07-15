abs = abs
for _ in range(int(input())):
    lst_s = [ord(i) for i in input()]
    length = len(lst_s)-1
    for i in range(length):
        if abs(lst_s[i]-lst_s[i+1]) != abs(lst_s[length-i]-lst_s[length-i-1]):
            print("Not Funny")
            break
    else:
        print("Funny")