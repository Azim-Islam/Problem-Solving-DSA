
from collections import deque
n = int(input())
arr = map(int, input().split())
stack = deque()


stack.append(arr[0])
i = 1
while True:
    if stack[0] >= arr[i]:
        stack.append(arr[i])