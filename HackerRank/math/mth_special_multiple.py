

def findVal(n):
    for i in nine_zeros:
        if i%n == 0:
            print(i)
            break
        elif i%n == n//2 and not n%2:
            print(i*10)
            break
        
def generateList():
    array = []
    for i in range(1, 500*500):
        array.append(int(bin(i)[2:].replace("1", "9")))
    return array
    
nine_zeros = generateList()
for _ in range(int(input())):
    n = int(input())
    findVal(n)