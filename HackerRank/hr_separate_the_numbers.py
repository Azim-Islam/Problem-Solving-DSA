#450451
int = int
for _ in range(int(input())):
    string = (input())
    ch_test = ""
    for i in range(1,len(string)):
        ch_test = string[:i]
        j = int(ch_test)
        while not len(ch_test) >= len(string):
            j = str(int(j)+1)
            ch_test = str(ch_test)+str(j)
        if ch_test==string:
            print("YES", string[:i])
            break
    else:
        print("NO")
