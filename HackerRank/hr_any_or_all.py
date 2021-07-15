n = int(input())
array = list(map(lambda x: True if x==x[::-1] else False, list(filter(lambda x: (x==x[::-1] or int(x) < 0), input().split()))))
print(all(array) and len(array)>0)