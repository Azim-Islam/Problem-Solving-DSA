from functools import lru_cache

# @lru_cache(None)
def search(h, w):
    global ans
    if (h == 20 and w == 19) or (h == 19 and w == 20):
        return 1
    elif h > 20 or w > 20:
        return 0
    else:
        print(h, w)
        ans += search(h+1, w)
        ans += search(h, w+1)
    return 1
h, w = map(int, input().split())
arr = []
# for i in range(h):
#     arr.append(list(input()))

ans = 0
search(1, 1)
print(ans)
