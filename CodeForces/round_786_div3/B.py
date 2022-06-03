for _ in range(int(input())):
    chars = input()
    pos = abs(ord('a')-ord(chars[0]))*25 + abs(ord('a')-ord(chars[1]))
    if chars[0] > chars[1]:
        pos += 1 
    print(pos)