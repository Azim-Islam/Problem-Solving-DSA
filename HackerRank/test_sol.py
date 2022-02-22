

import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    s=list(s)
    if n<=k:
        return '9'*n
    mink=[0]*(n//2+1)
    for i in range(n//2-1,-1,-1):
        if s[i]!=s[n-1-i]:
            mink[i]=mink[i+1]+1
        else:
            mink[i]=mink[i+1]
    if mink[0]>k:
        return '-1'
    i=0
    while i<n//2 and k>mink[i]:
        if s[i]=='9':
            if s[n-1-i]!='9':
                s[n-1-i]='9'
                k-=1
        elif s[n-1-i]=='9':
            s[i]='9'
            k-=1
        elif k-2>=mink[i+1]:
            s[i]=s[n-1-i]='9'
            k-=2
        else:
            if s[i]!=s[n-1-i]:
                s[i]=s[n-1-i]=max(s[n-1-i],s[i])
                k-=1
        i+=1
    if i<n//2:
        for j in range(i,n//2):
            if s[j]>s[n-1-j]:
                s[n-1-j]=s[j]
            else:
                s[j]=s[n-1-j]
    elif n%2:
        if k>0:
            s[n//2]='9'
    return ''.join(s)


if __name__ == '__main__':
    

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    print(highestValuePalindrome(s, n, k))