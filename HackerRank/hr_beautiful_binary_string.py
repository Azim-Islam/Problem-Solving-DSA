n = int(input())
string = input()
i = 0
count = 0
while i < n-2:
    if string[i:i+3] == "010":
        count += 1
        i += 3
    else:
        i += 1
print(count)