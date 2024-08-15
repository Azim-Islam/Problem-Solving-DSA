for _ in range(int(input())):
    s = input()
    
    t = str(int(s[0:2]) - 12*(int(s[0:2])//12))
    if len(t) == 1:
        t = "0"+t
    if t == "00":
        t = "12"
    print(t + s[2:]+ " PM"*(int(s[0:2])//12)+ " AM"*(not int(s[0:2])//12))