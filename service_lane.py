def calculate(*array):
    print(min(array))
n, t = map(int, input().split())
array_n = list(map(int, input().split()))
for _ in range(t):
    start, end = map(int, input().split())
    calculate(*array_n[start:end+1])