# abdc > acbd
# nmrcrni > nmricnr
def small_sort(string):
    og_string = string
    string = list(string)
    maxv = ['{', 0, 0]
    for i in range(len(string)-1, 0, -1):
        if string[i] > string[i-1]:
            for j in range(i, len(string)):
                if string[j] > string[i-1] and string[j] < string[i] and string[j] < maxv[0]:
                    maxv = [string[j], 1, j]
            if maxv[1] == 1:
                temp = string[i-1]
                string[i-1] = maxv[0]
                string[maxv[2]] = temp
            else:
                temp = string[i-1]
                string[i-1] = string[i]
                string[i] = temp
            #string[i:len(string)] = string[len(string)-1:i-1:-1]
            string[i:len(string)] = sorted(string[i:len(string)])
            return string
    return list("no answer")
for _ in range(int(input())):
    string = input()
    if len(string)==1:
        print("no answer")
    else:
        print(*small_sort(string), sep='')