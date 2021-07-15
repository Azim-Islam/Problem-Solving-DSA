from collections import Counter
def anagrams(lng, j, i,sub_str, string):
    #print(sub_str)
    counted = 0
    counted_sub = Counter(sub_str)
    k = j+1
    l = k+i
    while l <= lng:
        if  Counter(string[k:l]) == counted_sub:
            counted += 1
        k += 1
        l += 1
    return counted
for _ in range(int(input())):
    string = input()
    count = 0
    lng = len(string)
    for i in range(1, lng):
        for j in range(lng-(i-1)):
            sub_str = string[j:j+i]
            count += anagrams(lng, j, i, sub_str, string)
    print(count)