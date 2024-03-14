from functools import cmp_to_key


def solve():

    n, m = map(int, input().split())

    arr = []
    atk = []
    df = []


    for i in range(n):
        l = input().split()
        if l[0] == "ATK":
            atk.append(int(l[1]))
        else:
            df.append(int(l[1]))


    for i in range(m):
        arr.append(int(input()))





    arr.sort(reverse=True)
    atk.sort()
    df.sort()

    # print(jcards)

    ans1 = 0

    for k, v in zip(arr, atk):
        if k >= v:
            ans1 += k - v
        else:
            break


    arr = arr[::-1]
    atk = atk[::-1]
    df = df[::-1]

    ans2 = 0
    marked = [0]*len(arr)
    #goal is to defat all the cards
    for i in range(len(df)):
        fnd = False
        for j in range(m):
            if not marked[j] and arr[j] > df[i]:
                # print(arr[j], df[i])
                marked[j] = 1
                fnd = True
                break
            
        if not fnd:
            print(ans1)
            return

            
    for i in range(len(atk)):
        fnd = False
        for j in range(m):
            if not marked[j] and arr[j] >= atk[i]:
                marked[j] = 1
                # print(arr[j], atk[i])
                ans2 += arr[j] - atk[i]
                fnd = True
                break

        if not fnd:
            print(ans1)
            return

    

    for j in range(m):
        if not marked[j]:
            ans2 += arr[j]

    print(max(ans1, ans2))

solve()