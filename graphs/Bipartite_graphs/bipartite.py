# n --> number of nodes
# req:
# 1 arr of colors --> red = 1, green = 0, not visited = -1
# initialize the arr with -1 (meaing not visited)
# apply dfs and color them.
# Coloring criteria:
#   1. adjacent nodes can't have same color

from collections import deque

def main():
    def dfs(adj: dict[int, list[int]], node: int, color: list[int], i: int) -> bool:
        color[node] = i #current node color
        
        for nei in adj[node]:
            if color[nei] == color[node]:
                return False
            elif color[nei] == -1:
                # this node is not visited
                adjColor = 1 - color[node]
                color[nei] = adjColor
                if not dfs(adj, nei, color, adjColor):
                    return False
                    
        return True
        
    def bfs(adj: dict[int, list[int]], node: int, color: list[int], i:int)->bool:
        q = deque()
        q.append(node)
        
        color[node] = i
        while q:
            node = q.popleft()
            for nei in adj[node]:
                if color[nei] == color[node]:
                    return False
                    
                elif color[nei] == -1:
                    adjColor = 1 - color[node]
                    color[nei] = adjColor
                    q.append(nei)
                    
        return True
        
                    
    def isBipartite(n: int, adj: dict[int, list[int]]) -> bool:
        color = [-1]*n
        # -1 -> not visited
        # 1 -> red
        # 0 -> green
        for node in range(n):
            if color[node] == -1:
                if not bfs(adj, node, color, 1):
                    return False
        return True
        
        
    graph = {
        0: [1, 2],
        1: [0, 4],
        2: [0, 3, 4],
        3: [2],
        4: [1, 2, 5],
        5: [4]
    }
    
    n = len(graph)
    if isBipartite(n, graph):
        print("============================================")
        print("The Graph is Bipartite!")
        print("============================================")
    
if __name__ == "__main__":
    main()
    