for _ in range(int(input())):
    try:
        a, b = input().split()
        a = a.lower()
        b = b.lower()

        a = a.replace("p", "b")
        a = a.replace("i", "e")
        b = b.replace("p", "b")
        b = b.replace("i", "e")

        if len(a) != len(b):
            print("No")
        else:
            for i in range(len(a)):
                if a[i] != b[i]:
                    print("No")
                    break
            else:
                print("Yes")
    except:
        print("No")