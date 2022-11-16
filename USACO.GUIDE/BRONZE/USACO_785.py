from bisect import bisect_left
input = open("outofplace.in", "r")
print = lambda x : open("outofplace.out", "w").write(str(x)+"\n")

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

t_arr = arr[:]
t_arr.sort()

idx = []
# print(t_arr)
# print(arr)
for i in range(n):
    if t_arr[i] != arr[i]:
        idx.append(i)

print(max(0, len(idx)-1))