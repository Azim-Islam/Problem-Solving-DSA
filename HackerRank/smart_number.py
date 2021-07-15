import math

def is_smart_number(num):
    val = int(math.sqrt(num))
    if math.sqrt(num) == val: ## If the number is perfect square
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")



