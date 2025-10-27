def printDiagonal(matrix):
    if not matrix:
        return []
        
    m, n = len(matrix), len(matrix[0])
    result = []
    i, j = 0, 0
    dir = 1
    for _ in range(m*n):
        result.append(matrix[i][j])
        
        if dir == 1:
            if j == n-1:
                i += 1
                dir = -1
                
            elif i == 0:
                j += 1
                dir = -1
            else:
                i -= 1
                j += 1
                
        else:
            if i == m-1:
                j += 1
                dir = 1
            elif j == 0:
                i += 1
                dir = 1
            else:
                i += 1
                j -= 1
                
    return result
    
matrix = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]

print(printDiagonal(matrix))