def findfreinds(p):
    for nxt in relations[p]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        findfreinds(nxt)

for ro in range(int(input())):
    N, M = map(int,input().split())
    relations = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    for m in range(M):
        a, b = map(int,input().split())
        relations[a].append(b)
        relations[b].append(a)
    
    cnt = 0
    for p in range(1, N + 1):
        if visited[p]:
            continue
        
        cnt += 1
        visited[p] = True
        findfreinds(p)
    print('#%d %d' %(ro + 1, cnt))        
    