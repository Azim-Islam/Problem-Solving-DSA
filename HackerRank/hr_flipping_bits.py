def to32BitBin(n):
    n = bin(n)[2:].zfill(32)
    a = "1"*32
    return int(n, 2)^int(a, 2)

for _ in range(int(input())):
    n = int(input())
    print(to32BitBin(n))