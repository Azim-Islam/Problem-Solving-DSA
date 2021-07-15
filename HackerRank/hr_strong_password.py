n = int(input())
string = input()
numbers = set("0123456789")
lower_case = set("abcdefghijklmnopqrstuvwxyz")
upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
special_characters = set("!@#$%^&*()-+")
num = 1
lwr = 1
upr = 1
sc = 1
for i in string:
    if i in numbers:
        num = 0
    elif i in lower_case:
        lwr = 0
    elif i in upper_case:
        upr = 0
    elif i in special_characters:
        sc = 0
char_to_add = num+lwr+upr+sc
if n+char_to_add >= 6:
    print(char_to_add)
else:
    to_add = abs(char_to_add+n-6)
    print(char_to_add+to_add)
