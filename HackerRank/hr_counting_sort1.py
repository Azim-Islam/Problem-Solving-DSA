n = int(input())
lst_counted = [0]*100
array = list(map(int ,input().split()))
for i in array:
    lst_counted[i] += 1
for i in range(100):
    if lst_counted[i] > 0:
        print( (str(i)+' ')*lst_counted[i], end='')