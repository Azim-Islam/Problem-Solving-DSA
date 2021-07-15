for _ in range(int(input())):
    x, y = map(int, input().split())
    first_wins = [i for i in range(3, 16, 4)] + [i for i in range(4, 16, 4)]  
    print(first_wins)
    if x in first_wins or y in first_wins:
        print("First")
    else:
        print("Second")