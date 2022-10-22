import sys


input = sys.stdin.readline
n = input()
arr = list(map(int, input().split()))
print(len(set(arr)))