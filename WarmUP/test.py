def find(i):
    i = i + 1
    arr = [1]*i
    for j in range(1, i):
        for k in range(1, i):
            if k%j == 0:
                arr[k]  ^= 1
        # print(arr[1:])
    print(f"for n = {i-1} k = {sum(arr)  - 1}")


# for i in range(2, 2000):
    # find(i)
# find(2)
# find(11)
# find(11)

find(1030327)
