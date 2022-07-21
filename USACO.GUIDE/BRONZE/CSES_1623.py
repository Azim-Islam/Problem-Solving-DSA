n = int(input())
arr = list(map(int, input().split()))

min_diff = float('inf')
total_sum = sum(arr)
sum0 = 0

def func(k):
  global sum0, total_sum, min_diff
  if k == n:
      min_diff = min(abs(sum0-abs(sum0-total_sum)), min_diff)
  else:
    func(k+1)
    # print(f"adding {arr[k]}")
    sum0 += arr[k]
    func(k+1)
    # print(f"Removing {arr[k]}")
    sum0 -= arr[k]
    
func(0)

print(min_diff)