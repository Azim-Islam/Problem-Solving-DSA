def isPalindrome(string):
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

for _ in range(int(input())):
    string = list(input())

    i = 0
    j = len(string) - 1
    
    if isPalindrome(string):
        print("-1")
        continue

    while i < j:
        if string[i] != string[j]:
            if isPalindrome(string[i+1:j+1]):
                print(i)
                break
            elif isPalindrome(string[i:j]):
                print(j)
                break
        else:
            i += 1
            j -= 1
    