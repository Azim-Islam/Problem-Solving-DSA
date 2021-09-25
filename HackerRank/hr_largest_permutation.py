from collections import defaultdict


n, k = map(int, input().split())
array = list(map(int, input().split()))

ar_enum = defaultdict(int)

for i in range(n):
    ar_enum[array[i]] = i

j = 0
l = 0
if n > 1:
    for i in range(n, 0, -1):
        if i != array[j] and array[j] < i:
            ar_enum[i], ar_enum[array[j]] = ar_enum[array[j]], ar_enum[i] 
            array[ar_enum[array[j]]] = array[j]
            array[j] = i
            l += 1
            #print(*array)
            if l >= k:
                break
        j += 1
    
ar_enum = {j:i for (i,j) in ar_enum.items()}

for i in range(n):
    print(ar_enum[i], end=" ")