inputs = open('blocks.in', 'r')
print = lambda x : open('blocks.out', 'w').write(str(x)+'\n')


N = int(inputs.readline())
arr = [0]*26
for _ in range(N):
    word1, word2 = inputs.readline().split()
    word1_ = [0]*26
    word2_ = [0]*26
    for i in word1:
        word1_[ord(i)-97] += 1
    for i in word2:
        word2_[ord(i)-97] += 1
    for i,v in enumerate(zip(word1_, word2_)):
        arr[i] += max(v[0],v[1])

ans = "\n".join([str(i) for i in arr])

print(ans)