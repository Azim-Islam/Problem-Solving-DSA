def count_matching1s(s):
    m = 0
    chunks = s.split("0")
    for c in chunks:
        m = max(m, len(c)) 
    m = max(m, len(chunks[-1]+chunks[0])) if len(chunks) > 1 else m
    return m


for _ in range(int(input())):
    s = input()
    matches = count_matching1s(s)
    m = matches
    # if matches == 1:
    #     print("1")
    # elif matches == 0:
    #     print("0")
    if matches == len(s):
        print((matches**2))
    else:
        k = m//2+1
        print((m-k+1)*k)
        