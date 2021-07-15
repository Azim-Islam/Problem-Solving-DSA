def testDecentNumber(length):
    if length % 3 == 1:
        if length >= 10:
            print((length-10)*"5"+10*"3")
        else:
            print("-1")
    elif length % 3 == 0:
        print(length * "5")
    elif length % 3 == 2:
        print((length - 5) * "5" + 5 * "3")


for _ in range(int(input())):
    n = int(input())
    if n >= 3:
        testDecentNumber(n)
    else:
        print("-1")
