n, k = map(int, input().split())
array = sorted(map(int, input().split()))
count = 0
sum_ = 0
for i in array:
    if sum_+i <= k:
        count += 1
        sum_ += i
    else:
        break
print(count)