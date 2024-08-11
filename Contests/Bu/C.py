def isPalindrome(x):
    if x == x[::-1]:
        return True

def check(x):
    return isPalindrome(x)


for t in range(int(input())):
    n, k = map(int, input().split()) 
    s = list(input())
    sp = ['']*10**5
    if k <= n:
        sp = s[:k][::-1]
        if check(s + sp) and check(sp+s):
            print("Yes")
        else:
            print("No")
    else:
        # sp[:n] = s[::-1]
        # sp[-n:] = s[::-1]
        # print(sp)
        # if check(s + sp) and check(sp+s):
        #     print("Yes")
        # else:
        #     print("No")
        if k%n == 0:
            print("Yes")
        else:
            print("No")