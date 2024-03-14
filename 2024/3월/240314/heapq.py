# 귀여운 문제 >< 

import sys
import heapq

INF = float('inf')
input = sys.stdin.readline

def dijkstra(start, N, graph, dp, idx):
    dp[start][idx] = 0
    pq = [(0, start)]
    
    while pq:
        dist, now = heapq.heappop(pq)
        if dp[now][idx] < dist:
            continue
        for next_node, cost in graph[now]:
            next_dist = dist + cost
            if next_dist < dp[next_node][idx]:
                dp[next_node][idx] = next_dist
                heapq.heappush(pq, (next_dist, next_node))
                
N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
dp = [[INF] * 2 for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

dijkstra(1, N, graph, dp, 0) 
dijkstra(N, N, graph, dp, 1)

min_value = INF
prices = list(map(int, input().split()))

for i in range(1, N + 1):
    if prices[i-1] == -1:
        continue
    if dp[i][0] != INF and dp[i][1] != INF:
        min_value = min(min_value, dp[i][0] + dp[i][1] + prices[i-1] * (K-1))
        
print(min_value if min_value != INF else -1)
