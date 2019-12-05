for ro in range(int(input())):
    N, E = map(int,input().split())
    board = [[99999999999] * (N + 1) for _ in range(N + 1)]
    relations = [[] for _ in range(N + 1)]
    for _ in range(E):
        a, b, e = map(int,input().split())
        board[a][b] = e
        relations[a].append(b)
    visited = [False] * (N + 1)
    dist = [99999999999] * (N + 1)
    dist[0] = 0
    while True:
        min_dist = 99999999999
        min_idx = -1

        for idx in range(N + 1):
            if not visited[idx] and min_dist > dist[idx]:
                min_dist = dist[idx]
                min_idx = idx

        visited[min_idx] = True
        if visited[N]:
            break

        for nxt in relations[min_idx]:
            if not visited[nxt] and dist[nxt] > dist[min_idx] + board[min_idx][nxt]:
                dist[nxt] = dist[min_idx] + board[min_idx][nxt]

    print('#%d %d' %(ro + 1, dist[N]))

