class DSU:
    def __init__(self, n:int)-> None:
        self.parent = [i for i in range(n)]
        self.rank = [0]*n

    def find(self, x: int)-> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x: int, y:int)-> None:
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return

        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py

        else:
            self.parent[py] = px
            self.rank[px] += 1
        return

def main():
    
    def makeConnected(n: int, connections: list[list[int]]) -> int:
        extraEdge = 0
        comp = n
        edges = len(connections)
        if edges < n-1:
            return -1
    
        dsu = DSU(n)
        for u, v in connections:
            if dsu.find(u) == dsu.find(v): # part of same componnent
                extraEdge += 1
            else:
                dsu.union(u, v)
                comp -= 1
    
        if extraEdge >= comp - 1:
            return comp -1
        else:
            return -1
            
    connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
    n = len(connections)
    
    operations = makeConnected(n, connections)
    if operations != -1:
        print(f"{operations} are required!!")
    else:
        print("Not Possible!!")
        
        
if __name__ == "__main__":
    main()
    
