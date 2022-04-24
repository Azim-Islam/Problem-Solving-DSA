for _ in range(int(input())):
    string = input()
    curr_count = 0
    flag = True
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            curr_count += 1
        elif string[i] != string[i+1]:
            if curr_count == 0:
                print("NO")
                flag = False
                break
            else:
                curr_count = 0
    if curr_count == 0 and flag:
        print("NO")
    elif flag:
        print("YES")