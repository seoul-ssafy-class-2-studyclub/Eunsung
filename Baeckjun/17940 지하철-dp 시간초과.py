from heapq import heappush, heappop

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
            # adj[x].append(y)

queue = []
heappush(queue, (0, 0, 0, 1)) # 환승횟수, 총 비용, 현재위치, 현재상태

while queue:
    cnt, cost, now, status = heappop(queue)

    if now == G:
        break

    for nxt in adj[now]:
    # for nxt in range(N):
    #     if not subwayLine[now][nxt]:
    #         continue

        if status & (1 << nxt):
            continue

        if stations[now] == stations[nxt]:
            temp = 0
        else:
            temp = 1

        heappush(queue, (cnt + temp, cost + subwayLine[now][nxt], nxt, status | (1 << nxt)))

print(cnt, cost)
