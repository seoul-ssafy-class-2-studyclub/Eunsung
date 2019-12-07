from heapq import heappush, heappop
from math import inf

N, G = map(int,input().split())

stations = []
for station in range(N):
    stations.append(int(input()))

subwayLine = [0] * N
adj = [[] for _ in range(N)]
for y in range(N):
    subwayLine[y] = list(map(int,input().split()))
    for x in range(N):
        if subwayLine[y][x]:
            adj[y].append(x)

keys = [(0, inf)] * N

queue = []
status = 1
heappush(queue, (0, 0, 0))#환승횟수, 코스트, 현재위치

while queue:
    cnt, cost, now = heappop(queue)
    if now == G:
        break
    
    for nxt in adj[now]:
        if stations[now] == stations[nxt]:
            temp = 0
        else:
            temp = 1
        if status & (1 << nxt):
            if cnt > keys[nxt][0]:
                continue

            elif keys[nxt][1] > cost + subwayLine[now][nxt]:
                
                keys[nxt] = (cnt + temp, cost + subwayLine[now][nxt])
                heappush(queue, (cnt + temp, cost + subwayLine[now][nxt], nxt))
        else:
            status = status | (1 << nxt)
            keys[nxt] = (cnt + temp, cost + subwayLine[now][nxt])
            heappush(queue, (cnt + temp, cost + subwayLine[now][nxt], nxt))
print(cnt, cost)
        

