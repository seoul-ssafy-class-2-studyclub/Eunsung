from collections import deque

def dfs(now, nxt):
    if dp[now][nxt] or dp[nxt][now]:
        count[now] += 1
        count[nxt] += 1
        return True
    
    result = False
    for nnxt in adj[nxt]:
        if visited[nnxt]:
            continue
        visited[nnxt] = True
        if dfs(nxt, nnxt):
            dp[now][nxt] = 1
            return True

        visited[nnxt] = False
    return False
        
for ro in range(int(input())):
    N = int(input())
    M = int(input())

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    adj = [deque() for _ in range(N + 1)]
    count = [0] * (N + 1)
    
    for _ in range(M):
        a, b = map(int,input().split())
        dp[a][b] = 1
        adj[a].append(b)

    visited = [False] * (N + 1)

    for start in range(1, N + 1):
        visited[start] = True
        for nxt in range(1, N + 1):
            if start == nxt:
                continue
            visited[nxt] = True
            dfs(start, nxt)
            visited[nxt] = False
        visited[start] = False
    
    print(count)
    print(dp)
