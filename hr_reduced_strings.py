import re
string = input()
flag = 1
while 1: 
    length = len(string)
    string = re.sub(r"(.)\1", "", string)
    if len(string) == length:
        break
print(string*any(string), "Empty String"*(not any(string)), sep="")