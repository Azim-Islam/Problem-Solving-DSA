inputs = open('pails.in', 'r')
print = lambda x : open('pails.out', 'w').write(str(x)+'\n')

x, y, m = map(int, inputs.readline().split())

answers = []

a = m//x
b = m//y

answers = []
for i in range(0, a+1):
    count = i*x
    count += y * ((m-count)//y)
    answers.append(count)   

# for i in range(1, b+1):
#     count = i*y
#     count += x * ((m-count)//x)
#     answers.append(count)  

print(max(answers))