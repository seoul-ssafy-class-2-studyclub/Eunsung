def dfs(idx):
    for nxt in relations[idx]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        dfs(nxt)

for ro in range(int(input())):
    N, M = map(int,input().split())
    inp = list(map(int,input().split()))
    relations = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    for idx in range(M):
        relations[inp[idx * 2]].append(inp[idx * 2 + 1])
        relations[inp[idx * 2 + 1]].append(inp[idx * 2])

    cnt = 0
    for per in range(1, N + 1):
        if visited[per]:
            continue
        visited[per] = True
        dfs(per)
        cnt += 1

    print('#%d %d' %(ro + 1, cnt))
