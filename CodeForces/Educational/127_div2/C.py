

for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    sum_  = 0
    build = []
    for i in arr:
        if sum_ + i <= x:
            sum_ += i
            build.append(i)

    total = 0
    i = 0
    while len(build) != 0:
        while sum_ > x:
            sum_ = sum_ - (build.pop()+i)
        if x-sum_ >= len(build) and len(build) > 0:
            factor = (x-sum_)//len(build)
            i += factor
            sum_ += factor*len(build)
            total += len(build)*factor
        else:
            total += len(build)
            i += 1
            sum_ += len(build)

    print(total)