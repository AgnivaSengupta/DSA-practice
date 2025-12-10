import heapq

def main():
    def dijkstra(adj:dict[int, list[tuple[int, int]]], src:int) -> list[float]:
        n = len(adj)
        dist = [float("inf")]*n
        dist[src] = 0
        pq = [(0.0, src)]     #(node, dist)
        while pq:
            curr_dist, node = heapq.heappop(pq)
            
            if curr_dist > dist[node]:
               continue
           
            for v, w in adj[node]:
                if dist[node] + w < dist[v]:
                    dist[v] = dist[node] + w
                    heapq.heappush(pq, (dist[v], v))
        return dist
        
    adj = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    
    print(dijkstra(adj, 0))

if __name__ == '__main__':
    main()
