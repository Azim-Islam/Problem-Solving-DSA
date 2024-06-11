from collections import deque

from sys import stdin, stdout


def insert_count_bits(count, ai):
    for i in range(20):
        if (1 << i)&ai:
            count[i] += 1
    
def extract_count_bits(count, ai):
    for i in range(20):
        if (1 << i)&ai:
            count[i] -= 1
        

def build_or(count):
    number = []
    number.append("0b")
    for i in range(20):
        if count[i]:
            number.append("1")
        else:
            number.append("0")
    return int("".join(number), base=0)


def check(arr, k):
    count = [0]*20
    q = deque([])
    for i in range(k):
        q.append(arr[i])
        insert_count_bits(count, arr[i])
    
    a_OR = build_or(count)
    for i in range(0, len(arr)-k):
        v = q.popleft()
        extract_count_bits(count, v)
        q.append(arr[i+k])
        insert_count_bits(count, arr[i+k])

        t_OR = build_or(count)
        # print(q, count)
        if t_OR != a_OR:
            return 0
    
    return 1




input = stdin.readline
ans = []
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    lo = 1 
    hi = n
    while lo < hi:
        mid = (lo+hi)//2
        if check(arr, mid):
            hi = mid
        else:
            lo = mid + 1
    ans.append(str(hi))

print("\n".join(ans), file=stdout)