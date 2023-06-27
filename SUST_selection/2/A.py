import sys;
from math import ceil,log2,log;
INT_MAX = sys.maxsize;
#segment trees https://www.geeksforgeeks.org/segment-tree-range-minimum-query/ https://www.geeksforgeeks.org/segment-tree-set-2-range-maximum-query-node-update/?ref=rp
 
class segmentMax:
    def getMid(s, e):
        return s + (e - s) // 2

    def MaxUtil(st, ss, se, l, r, node):

        if (l <= ss and r >= se):
            return st[node]
        if (se < l or ss > r):
            return -1

        mid = segmentMax.getMid(ss, se)
    
        return max(segmentMax.MaxUtil(st, ss, mid, l, r,
                        2 * node + 1),
                segmentMax.MaxUtil(st, mid + 1, se, l,
                        r, 2 * node + 2))

    def updateValue(arr, st, ss, se, index, value, node):
        if (index < ss or index > se):
            print("Invalid Input")
            return
    
        if (ss == se):
    

            arr[index] = value
            st[node] = value
        else:
            mid = segmentMax.getMid(ss, se)
    
            if (index >= ss and index <= mid):
                segmentMax.updateValue(arr, st, ss, mid, index,
                            value, 2 * node + 1)
            else:
                segmentMax.updateValue(arr, st, mid + 1, se,
                            index, value, 2 * node + 2)
    
            st[node] = max(st[2 * node + 1],
                        st[2 * node + 2])
        return
    

    
    def getMax(st, n, l, r):
    

        if (l < 0 or r > n - 1 or l > r):
            print("Invalid Input")
            return -1
    
        return segmentMax.MaxUtil(st, 0, n - 1, l, r, 0)

    def constructSTUtil(arr, ss, se, st, si):
    

        if (ss == se):
            st[si] = arr[ss]
            return arr[ss]

        mid = segmentMax.getMid(ss, se)
    
        st[si] = max(segmentMax.constructSTUtil(arr, ss, mid, st,
                                    si * 2 + 1),
                    segmentMax.constructSTUtil(arr, mid + 1, se,
                                    st, si * 2 + 2))
    
        return st[si]

    
    
    def constructST(arr, n):
    
        # Height of segment tree
        x = ceil(log(n, 2))
    
        # Maximum size of segment tree
        max_size = 2 * pow(2, x) - 1
    
        # Allocate memory
        st = [0]*max_size
    
        # Fill the allocated memory st
        segmentMax.constructSTUtil(arr, 0, n - 1, st, 0)
    
        # Return the constructed segment tree
        return st

###########
class segmentMin:
    def minVal(x, y) :
        return x if (x < y) else y; 
    
    # A utility function to get the 
    # middle index from corner indexes. 
    def getMid(s, e) :
        return s + (e - s) // 2; 
    
    """ A recursive function to get the 
    minimum value in a given range 
    of array indexes. The following 
    are parameters for this function. 
    
        st --> Pointer to segment tree 
        index --> Index of current node in the 
            segment tree. Initially 0 is 
            passed as root is always at index 0 
        ss & se --> Starting and ending indexes 
                    of the segment represented 
                    by current node, i.e., st[index] 
        qs & qe --> Starting and ending indexes of query range """
    def RMQUtil( st, ss, se, qs, qe, index) :
    
        # If segment of this node is a part 
        # of given range, then return 
        # the min of the segment 
        if (qs <= ss and qe >= se) :
            return st[index]; 
    
        # If segment of this node 
        # is outside the given range 
        if (se < qs or ss > qe) :
            return INT_MAX; 
    
        # If a part of this segment 
        # overlaps with the given range 
        mid = segmentMin.getMid(ss, se); 
        return segmentMin.minVal(segmentMin.RMQUtil(st, ss, mid, qs, 
                            qe, 2 * index + 1), 
                    segmentMin.RMQUtil(st, mid + 1, se,
                            qs, qe, 2 * index + 2)); 
    
    # Return minimum of elements in range 
    # from index qs (query start) to 
    # qe (query end). It mainly uses RMQUtil() 
    def RMQ( st, n, qs, qe) : 
    
        # Check for erroneous input values 
        if (qs < 0 or qe > n - 1 or qs > qe) :
        
            print("Invalid Input"); 
            return -1; 
        
        return segmentMin.RMQUtil(st, 0, n - 1, qs, qe, 0); 
    
    # A recursive function that constructs 
    # Segment Tree for array[ss..se]. 
    # si is index of current node in segment tree st 
    def constructSTUtil(arr, ss, se, st, si) :
    
        # If there is one element in array, 
        # store it in current node of 
        # segment tree and return 
        if (ss == se) :
    
            st[si] = arr[ss]; 
            return arr[ss]; 
    
        # If there are more than one elements, 
        # then recur for left and right subtrees 
        # and store the minimum of two values in this node 
        mid = segmentMin.getMid(ss, se); 
        st[si] = segmentMin.minVal(segmentMin.constructSTUtil(arr, ss, mid,
                                        st, si * 2 + 1),
                        segmentMin.constructSTUtil(arr, mid + 1, se,
                                        st, si * 2 + 2)); 
        
        return st[si]; 
    
    def constructST(arr, n) :
        x = (int)(ceil(log2(n))); 
        max_size = 2 * (int)(2**x) - 1; 
        st = [0] * (max_size); 

        segmentMin.constructSTUtil(arr, 0, n - 1, st, 0); 
    
        return st; 
  


    #print("Minimum of values in range [", qs, ",", qe, "]", "is =", RMQ(st, n, qs, qe)); 
  
# This code is contributed by AnkitRai01 

n, k = map(int, input().split())
arr = list(map(int, input().split()))

mn = segmentMin.constructST(arr, n); #to find the min
mx = segmentMax.constructST(arr, n) #to find the max

ans1 = []
ans2 = []
for i in range(0, n-k+1):
    ans1.append(segmentMin.RMQ(mn, n, i, i+k-1))
    ans2.append(segmentMax.getMax(mx, n, i, i+k-1))

print(" ".join(map(str, ans1)))
print(" ".join(map(str, ans2)))
