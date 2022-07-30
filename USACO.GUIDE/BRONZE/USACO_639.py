

inputs = open('diamond.in', 'r')
print = lambda x : open('diamond.out', 'w').write(str(x)+'\n')

n, k = map(int, inputs.readline().split())

arr = []
for _ in range(n):
    arr.append(int(inputs.readline()))

arr.sort()

count = 0
answers = []
for i in range(n):
    count = 1
    for j in range(i+1, n):
        if abs(arr[i]-arr[j]) <= k:
            count += 1
    answers.append(count)

print(max(answers)) 