n, d = map(int, input().split())
array = list(map(int, input().split()))
count = 0 
array_dict = {i:1 for i in array}
for i in array:
    val = i
    flag = 1
    for _ in range(2):
        val = val+d
        if array_dict.get(val)==1:
            pass
        else:
            flag = 0
            break
    if flag == 1:
        count += 1 
print(count)