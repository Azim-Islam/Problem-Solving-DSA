from os import sep
n = int(input())
string = input().strip()
k = int(input())
str_crypted = []
ord = ord
chr = chr
for i in string:
    int_char = ord(i)
    if int_char >= 65 and int_char <= 90:
        tmp = int_char+k%26
        if tmp > 90:
            tmp = 65+tmp-90-1
        str_crypted.append(chr(tmp))
    elif int_char >= 97 and int_char <= 122:
        tmp = int_char+k%26
        if tmp > 122:
            tmp = 97+tmp-122-1
        str_crypted.append(chr(tmp))
    else:
        str_crypted.append(i)
print(*str_crypted, sep='')