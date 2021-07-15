n = int(input())
array = sorted(map(int, input().split()), reverse=True)
array = [2**j*i for i,j in zip(array, range(0, n))]
print(sum(array))