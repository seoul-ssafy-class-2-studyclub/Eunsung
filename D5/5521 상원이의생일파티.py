for ro in range(int(input())):
    N, M = map(int,input().split())
    relations = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    for idx in range(M):
        a, b = map(int,input().split())
        relations[a].append(b)
        relations[b].append(a)
    
    queue = [1]
    cnt = 0

    for _ in range(2):
        for _ in range(len(queue)):
            now = queue.pop(0)

            for nxt in relations[now]:
                if visited[nxt] or nxt == 1:
                    continue
                visited[nxt] = True
                queue.append(nxt)
                cnt += 1
    
    print('#%d %d' %(ro + 1, cnt))
