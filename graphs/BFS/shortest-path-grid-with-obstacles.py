from collections import deque

def bfs(matrix, k):
    m = len(matrix)
    n = len(matrix[0])

    if m == 1 and n == 1:
        return 0
# ==================================================================================================================
    if k >= m + n - 3:          # This is a very important Optimization. Without it it will show MLE for large k
        return m + n - 2        # This is called MANHATTAN DISTANCE
# ==================================================================================================================
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()
    q.append((0, 0, k))  # (i, j, k)
    visited = set()
    visited.add((0, 0, k))
    step = 0
    while q:
        for _ in range(len(q)):
            x, y, k = q.popleft()
            for dx, dy in delta:
                if x + dx == m - 1 and y + dy == n - 1:
                    return step + 1
                if (
                    x + dx < m
                    and x + dx > -1
                    and y + dy < n
                    and y + dy > -1
                    and (x + dx, y + dy, k) not in visited
                ):
                    if matrix[x + dx][y + dy] == 1 and k - 1 != -1:
                        q.append((x + dx, y + dy, k - 1))
                        visited.add((x + dx, y + dy, k - 1))
                    elif matrix[x + dx][y + dy] == 0:
                        q.append((x + dx, y + dy, k))
                        visited.add((x + dx, y + dy, k))
                    else:
                        continue
        step += 1
    return -1


grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
]
k = 27

print(bfs(grid, k))
