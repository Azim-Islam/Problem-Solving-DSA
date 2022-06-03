inputs = open('shuffle.in', 'r')
print = lambda x : open('shuffle.out', 'w').write(str(x))

N = int(inputs.readline())
arr = list(map(int, inputs.readline().split()))
ids = list(inputs.readline().rstrip().split())

for i in range(3):
    tmp_arr = [0]*N
    for index, value in enumerate(arr):
        tmp_arr[index] = ids[value-1]
    ids = tmp_arr

print("\n".join(ids))