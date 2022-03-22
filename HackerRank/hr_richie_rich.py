n, k = map(int, input().split())
string = input()

first_half = []
last_half = []
middle = []
mismatches = 0 
count = 0

for i in range(0, n//2):
    first_half.append(string[i])
    last_half.append(string[-(i+1)])
    if first_half[i] != last_half[i]:
        mismatches += 1

max_dswaps = k - mismatches
# print(f"mismatechs {mismatches} {n} {k}")

for i in range(n//2):
    if k-2 >= 0 and max(last_half[i], first_half[i]) != '9' and mismatches <= k-1:
        if first_half[i] != last_half[i]:
            mismatches -= 1
        first_half[i] = '9'
        last_half[i] = '9'
        k -= 2
    elif k-1 >= 0: 
        if first_half[i] != last_half[i]:
            first_half[i] = max(first_half[i], last_half[i])
            last_half[i] = max(first_half[i], last_half[i])
            k -= 1
            mismatches -= 1
    elif k < 1 and mismatches > 0:
        print("-1")
        exit()
#    print(f"{mismatches} {k}")


# if k >= 2:
#     for i in range(n//2):
#         if k-2 >= 0 and first_half[i] != '9' and last_half[i] != '9':
#             first_half[i] = '9'
#             last_half[i] = '9'
#             k -= 2
if n%2:
    middle.append(string[n//2])
    if k > 0:
        middle[0] = '9'
        k -= 1

print("".join(first_half+middle+last_half[::-1]))
