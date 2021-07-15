from math import ceil, floor
s = input().replace(" ", "")
n = len(s)
columns = ceil(n**0.5)
rows = floor(n**0.5)
'''while columns*rows < n:
    if (columns+1)*rows == n and (columns-rows) == -1:
        columns += 1
    elif (columns)*(rows+1) == n and (rows-columns) == -1:
        rows += 1
    else:
        if rows < columns:
            rows += 1
        else:
            columns += 1'''
    
j = 0
for i in range(columns):
    while True:
        try:
            print(s[i], end='')
            i+=columns
        except:
            print(' ', end='')
            break
