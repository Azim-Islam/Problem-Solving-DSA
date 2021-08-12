n = input()
array = [0]
array += list(map(int, input().split()))

for _ in range(int(input())):
    x, y = map(int, input().split())
    if(array[x]%2) or (len(array) > x+1 and array[x+1] == 0 and y>x):
            print("Odd")
    else:
        print("Even")