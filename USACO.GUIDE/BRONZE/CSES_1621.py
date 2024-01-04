import sys


input = sys.stdin.readline
n = input()
arr = input().split()
print(len(set(arr)), file=sys.stdout)