from math import gcd

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    barr = list(map(int, input().split()))

    pref_arr = [0]*n
    pref_arr[0] = arr[0]
    suff_arr = [0]*n
    suff_arr[n-1] = arr[n-1]
    
    pref_barr = [0]*n
    pref_barr[0] = barr[0]
    suff_barr = [0]*n
    suff_barr[n-1] = barr[n-1]

    for i in range(1, n):
        pref_arr[i] = gcd(pref_arr[i-1], arr[i])
        pref_barr[i] = gcd(pref_barr[i-1], barr[i])
    
    for i in range(n-2, -1, -1):
        suff_arr[i] = gcd(suff_arr[i+1], arr[i])
        suff_barr[i] = gcd(suff_barr[i+1], barr[i])

    ans = max(pref_arr[-1] + pref_barr[-1], suff_arr[0]+suff_barr[0])
    print(pref_arr, pref_barr)
    for i in range(1, n-1):
        aa = gcd(suff_arr[i+1], pref_arr[i-1])
        bb = gcd(suff_barr[i+1], pref_barr[i-1])
        ans = max(ans, gcd(bb, arr[i])+gcd(aa, barr[i]))

    print(ans)