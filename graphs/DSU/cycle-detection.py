class DSU:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n

    def find(self, x:int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x:int, y:int):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return True

        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return False

def main():
    def isCycle(adj: dict[int, list[int]])-> None:
        n = len(adj)
        dsu = DSU(n)
        for node in adj:
            for nei in adj[node]:
                if node < nei:      # to process each edge only once (Assumtion the nodes are named from 0 - n-1)
                    if dsu.union(node, nei):
                        print("There is cycle!!")
                        return

        print("There is no graph")
        return

    graph = {
            0: [1, 2],
            1: [0, 4],
            2: [0, 3, 4],
            3: [2],
            4: [1, 2, 5],
            5: [4]
        }

    isCycle(graph)


if __name__ == "__main__":
    main()