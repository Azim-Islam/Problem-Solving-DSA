from collections import Counter
n = int(input())
arr1 = Counter(map(int, input().split()))
m = int(input())
arr2 = Counter(map(int, input().split()))
ans = arr2-arr1
print(sorted(ans.keys()))