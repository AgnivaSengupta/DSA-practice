from collections import defaultdict


def countOverlaps(a, b, r_Off, c_Off):
    count = 0
    n = len(a)
    for i in range(n):
        for j in range(n):
            b_i = i + r_Off
            b_j = j + c_Off
            
            if b_i < 0 or b_i >= n or b_j < 0 or b_j >= n:
                continue
            elif a[i][j] == b[b_i][b_j] and a[i][j] == 1:
                count += 1               
    return count

def largestOverlap(a, b):
    n = len(a)
    maxOverlap = 0
    for i in range(-n+1, n, 1):
        for j in range(-n+1, n, 1):
            count = countOverlaps(a, b, i, j)
            maxOverlap = max(maxOverlap, count)
            
    return maxOverlap
    
img1 = [[1,1,0],[0,1,0],[0,1,0]]
img2 = [[0,0,0],[0,1,1],[0,0,1]]

print(largestOverlap(img1, img2))
# This is a brute force approach --> O(n^4) Time complexity
# for each offset we are traversing through the entire matrix
# Not Recommended much
# 
# ===================================================================================================
# ===================================================================================================
# Second Approach: VECTOR TRANSLATION COUNTING --> O(n^2) time complexity
# Main idea is for each translation vector, there are number of pairs of 1 that overlap
# We store them in a dict
# 
# if a[x1][y1] == 1 and b[x2][y2] == 1 then ((x2-x1), (y2-y1)) is the translation matrix

def vector_approach(a, b):
    n = len(a)
    a_ones = [(i, j) for i in range(n) for j in range(n) if a[i][j]]
    b_ones = [(i, j) for i in range(n) for j in range(n) if b[i][j]]
    
    count = defaultdict(int)
    for ax, ay in a_ones:
        for bx, by in b_ones:
            count[(bx-ax, by-ay)] += 1
            
    return max(count.values(), default=0)
    
print(vector_approach(img1, img2))