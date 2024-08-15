import string
from collections import defaultdict
import sys
vowels = {"a":0, "e":1, "i": 2, "o":3, "u":4}
consonents = {v:k for k, v in enumerate(sorted(string.ascii_lowercase-vowels.keys()))}

vowels_x = {v:k for (k,v) in vowels.items()}
consonents_x = {v:k for (k,v) in consonents.items()}


for _ in range(int(input())):
    count = defaultdict(int)
    string = sys.stdin.readline()[:-1]
    encrypted = []

    for s in string:
        k = count[s] 
        if s in vowels:
            chipher_char = consonents_x[(5*k+vowels[s])%21]
        else:
            chipher_char = vowels_x[(21*k+consonents[s])%5]

        encrypted.append(chipher_char)

        count[s] += 1
    
    print("".join(encrypted))