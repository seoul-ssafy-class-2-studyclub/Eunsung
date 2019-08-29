for ro in range(int(input())):
    V, E = map(int,input().split())

    routes = [[] for _ in range(V + 1)]
    visited = [False for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())

        routes[a].append(b)
        routes[b].append(a)
    start, end = map(int,input().split())

    queue = [(start,0)]
    visited[start] = True

    result = 0
    
    while queue:
        node = queue.pop(0)
        t = node[1]
        if node[0] == end:
            result = t
            break

        for nxt in routes[node[0]]:

            if visited[nxt]:
                continue
            visited[nxt] = True
            queue.append((nxt, t + 1))
    
    print('#%d %d' %(ro + 1, result))
            

        

