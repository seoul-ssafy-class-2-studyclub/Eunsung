from collections import deque

def dfs(now, nxt):
    if dp[now][nxt]:
        count[now] += 1
        return True
    
    result = False
    for nnxt in adj[nxt]:
        if visited[nnxt]:
            continue
        visited[nnxt] = True
        if dfs(nxt, nnxt):
            dp[now][nxt] = 1
            dp[nxt][now] = 1
            count[now] += 1

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
        dp[b][a] = 1
        adj[a].append(b)
        adj[b].append(a)
        count[a] += 1
        count[b] += 1

    visited = [False] * (N + 1)

    for start in range(1, N + 1):
        visited[start] = True
        for nxt in range(start + 1, N + 1):
            visited[nxt] = True
            dfs(start, nxt)
            visited[nxt] = False
        visited[start] = False
    
    print(count)
    print(dp)
