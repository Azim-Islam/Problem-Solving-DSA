n = int(input())
array = sorted(list(map(int, input().split())))
i = 0
j = 1
abs = abs
min_ = abs(array[i]-array[j])
for i in range(n-1):
    if abs(array[i]-array[i+1]) < min_:
        min_ = abs(array[i]-array[i+1])
print(min_)
