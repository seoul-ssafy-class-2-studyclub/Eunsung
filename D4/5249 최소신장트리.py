# def prims(now):
#     global cnt

#     min_nxt = 99999
#     min_idx = 0
#     for nxt in relations[now]:
#         if visited[nxt]:
#             continue
#         if dist[nxt] > board[now][nxt]:
#             dist[nxt] = board[now][nxt]
        

for ro in range(int(input())):
    V, E = map(int,input().split())
    board = [[99999] * (V + 1) for _ in range(V + 1)]
    relations = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    dist = [99999] * (V + 1) 
    dist[0] = 0
    cnt = 1
    for _ in range(E):
        a, b, e = map(int,input().split())
        board[a][b] = e
        board[b][a] = e
        relations[a].append(b)
        relations[b].append(a)
    
    for _ in range(V + 1):
        min_idx = -1
        min_dis = 99999

        for nxt in range(V + 1):
            if not visited[nxt] and dist[nxt] < min_dis:
                min_dis = dist[nxt]
                min_idx = nxt
        visited[min_idx] = True

        for nei in relations[min_idx]:
            if not visited[nei] and dist[nei] > board[min_idx][nei]:
                dist[nei] = board[min_idx][nei]
    print('#%d %d' %(ro + 1, sum(dist)))

            
    
    