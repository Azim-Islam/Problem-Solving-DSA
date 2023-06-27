input = open('split.in', 'r').readline
fout = open('split.out', 'w')

n = int(input())
cords = []


def solve(cords):
    cords.sort()

    y_min_left = [float('inf')]
    y_min_right = [float('inf')]
    
    y_max_left = [0]
    y_max_right = [0]
    
    n = len(cords)

    """
        To find the Height for the Left Area: We create two min-max prefix arrays from (left -> right co-ordinates) to find the height in O(1).
        To find the Height for the Right Area: We create two min-max prefix arrays from (right -> left co-ordinates) to find the height in O(1).
    """
    for i in range(n):
        y_min_left.append(y_min_left[-1] if y_min_left[-1] < cords[i][1] else cords[i][1])
        y_max_left.append(y_max_left[-1] if y_max_left[-1] > cords[i][1] else cords[i][1])
        y_min_right.append(y_min_right[-1] if y_min_right[-1] < cords[-i-1][1] else cords[-i-1][1])
        y_max_right.append(y_max_right[-1] if y_max_right[-1] > cords[-i-1][1] else cords[-i-1][1])
    

    y_min_right.reverse() #Reverse to synchronize indexing with our main iterator.
    y_max_right.reverse()

    main_area = abs(y_min_left[-1]-y_max_left[-1])*abs(cords[0][0]-cords[-1][0])
    ra = 0
    la = 0
    ans = 0
    for i in range(0, n-1):
        la = abs(cords[0][0]-cords[i][0])*abs(y_min_left[i+1]-y_max_left[i+1]) # i+1 since we have extra elem. initially.
        ra = abs(cords[i+1][0]-cords[-1][0])*abs(y_min_right[i+1]-y_max_right[i+1])
        # print(main_area - (ra+la))
        ans = max(ans, main_area - (ra+la))
    return ans

for i in range(n):
    cords.append(list(map(int, input().split())))


"""
    We move a vertical line through our co-ordinates and calculate the left area separated by
    the vertical line and also the right area separated by the vertical line.
    We can do this by sorting the co-ordinates by the x-axis,
    For a iterator 'i'
        The left area's width is:  sorted co-ordinate`s first elem.[x] <-----------> sorted co-ordinate`s 'i'th elem.[x]
        The left area's height is: ~check line 38

        The right area's width is: sorted co-ordinate`s 'i+1'th elem.[x] <-----------> sorted co-ordinate`s LAST elem.[x]
        The right area's height is: ~check line 39
"""
area_vertical_check = solve(cords)
#We swap x <-> y and re-run the algorithm, since area can be saved from the 'y' axis as-well.
cords = [[j, i] for i,j in cords]
area_horizontal_check = solve(cords)
#Otherwise test case 4, 10 will fail.
print(max(area_vertical_check, area_horizontal_check), file=fout)