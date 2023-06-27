for _ in range(int(input())):
    s = input()
    c = 0

    for i in range(1, len(s)):
        if s[i] == '_':
            if s[i-1] != "^":
                c += 1

    if len(s) == 1 and s[0] == "^":
        c += 1
    
    if s[-1] == '_':
        c += 1
    if s[0] == '_':
        c += 1
    
    print(c)