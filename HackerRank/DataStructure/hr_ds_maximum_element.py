#!/bin/python3

from collections import defaultdict
from email.policy import default
import bisect
import heapq
import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    stack = []
    max_val = []
    val_count = defaultdict(int)
    heap = []
    for op in operations:
        if op[0] == "1":
            _, val = map(int, op.split())
            stack.append(val)
            if val_count[val] == 0:
                bisect.insort_right(heap, val)
            val_count[val] += 1
        else:
            if op[0] == "2":
                popped = stack.pop()
                val_count[popped] -= 1
            elif op[0] == "3":
                while 1:
                    if val_count[heap[-1]] > 0:
                        max_val.append(heap[-1])
                        #print(heap)
                        break
                    else:
                        heap.pop()
    return max_val

if __name__ == '__main__':
    n = int(input().strip())
    ops = []
    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    print('\n'.join(map(str, res)))