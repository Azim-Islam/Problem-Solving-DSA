import sys

for _ in range(int(input())):
    numbers = []
    for _ in range(int(input())):
        string = sys.stdin.readline()[:-1]
        numbers.append(string)
        
    numbers.sort()
    for i in range(len(numbers)-1):
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            print("NO")
            break
    else:
        print("YES")
        
    #print(numbers)