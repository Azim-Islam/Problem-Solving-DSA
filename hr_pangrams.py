string = set(input().lower())
if len(string) == 27:
    print("pangram")
else:
    print("not pangram")
print(sorted(string))