n = int(input())
array = list(map(int, input().split()))
sorted_arr = (sorted(array))
flag = 0
indexes = []
for i in range(n-1):
    if array[i]>array[i+1]:
        flag -= 2
        indexes.append(i)
        indexes.append(i+1)
if flag == 0:
    print("yes")
elif flag == -2 or flag == -4:
    tmp = array[indexes[0]] 
    array[indexes[0]] = array[indexes[-1]]
    array[indexes[-1]] = tmp
    if array == sorted_arr:
        print("yes\nswap", indexes[0]+1, indexes[-1]+1)
    else:
        print("no"*(flag==-2))
else:
    if flag < -2:
        array[indexes[0]:indexes[-1]+1] = array[indexes[0]:indexes[-1]+1][::-1]
        #print(array)
        if array == sorted_arr:
            print("yes\nreverse", indexes[0]+1, indexes[-1]+1)
        else:
            print("no")
    else:
        print("no")
print(flag, indexes)