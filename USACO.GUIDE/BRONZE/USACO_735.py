inputs = open('lostcow.in', 'r')
print = lambda x : open('lostcow.out', 'w').write(str(x)+'\n')

x, y = map(int, inputs.readline().split())
array = [0]*3082
rel = 3082//4 #marks the 0th pos
array[rel+y] = 100
total_distance = 0
rel += x
i = 1
togo = 1
sign = +1
while True:
    for i in range(1, togo+1):
        total_distance += 1
        if array[rel+i*sign] == 100:
            print(total_distance)
            exit(0)
    total_distance += togo
    sign *= -1
    togo = togo*2