# Question: You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
#We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

from collections import defaultdict
import heapq
from typing import Any

def networkDelayTime(times: list[list[int]], n: int, k: int) -> Any:
    adj = defaultdict(list)
    for u, v, w in times:
        adj[u].append((v, w))
    
    dist = [float("inf")]*(n+1)
    dist[k] = 0 
    pq = [(0, k)]
    while pq:
        curr_dist, node = heapq.heappop(pq)

        if dist[node] < curr_dist:
            continue

        for v, w in adj[node]:
            if dist[node] + w < dist[v]:
                dist[v] = dist[node] + w
                heapq.heappush(pq, (dist[v], v))

    minTime = max(dist[1:])
    if minTime == float("inf"):
        return -1
    return minTime
    
