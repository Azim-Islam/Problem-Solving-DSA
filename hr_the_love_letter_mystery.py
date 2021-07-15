for _ in range(int(input())):
    string = list(map(lambda x:ord(x), input()))
    i = 0
    j = len(string)-1
    count = 0
    while i<j:
        if string[i] > string[j]:
            count += string[i] - string[j]
        elif string[j] > string[i]:
            count += string[j] - string[i]
        i += 1
        j -= 1
    print(count)