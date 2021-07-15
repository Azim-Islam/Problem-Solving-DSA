import re
def findPattern(grid, pattern, R, C, r, c):
    x = 0 
    y = 0
    i = 0
    j = 0
    '''Row Check'''
    '''Column Check'''
    while y<R:
        x = 0
        while x<C:   
            if pattern[j][i] == grid[y][x]:
                i += 1
            else:
                i = 0
            if i == c:
                x1 = x - (c-1)
                y1 = y+1
                k = 1
                l = 0
                flag = 1
                while k < r:
                    y1 = y+1
                    while l < c:
                        try:
                            if pattern[k][l] == grid[y1][x1]:
                                #print(grid[y1][x1])
                                y1 += 1
                                k += 1
                            else:
                                flag = 0
                                break
                        except:
                            flag = 0
                            break
                        if k == r:
                            k = 1
                            y1 = y+1
                            l += 1
                            x1 = x1+1
                        if l == c:
                            return True
                    if flag == 0:
                        try:
                            if grid[y][x+1] == grid[y][x]:
                                i -= 1
                            else:
                                i = 0
                        except:
                            i = 0
                        break
            #print(y, x)
            x += 1
        y = y+1
    return False
for _ in range(int(input())):
    no = 1
    R, C = map(int, input().split())
    grid = [[0]*C]*R
    for i in range(R):
        #grid[i] = list((map(int, list(input()))))
        grid[i] = input()
    r, c = map(int, input().split())
    pattern = [[0]*c]*r
    for i in range(r):
        #pattern[i] = list(map(int, list(input())))
        pattern[i] = input()
    if R==C==1:
        if pattern[0][0] == grid[0][0]:
            print("YES")
        else:
            print("NO")
        continue
    if findPattern(grid, pattern, R, C, r, c):
        print("YES")
    else:
        print("NO")
