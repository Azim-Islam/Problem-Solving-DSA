x, n = map(int, input().split())
lights = set([0, x])
gaps = [x]

for p in map(int, input().split()):
    lights.add(p)
    left = max(lights)
    right = min(lights)
    gaps.remove(right - left)
    gaps.append(p - left)
    gaps.append(right - p)
    print(max(gaps))