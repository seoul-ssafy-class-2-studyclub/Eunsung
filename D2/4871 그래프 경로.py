def dfs(start,goal):
    if route[start][goal]:
        return 1
    
    for i in range(1, V + 1):
        if route[start][i]:
            route[start][i] = 0
            if dfs(i,goal):
                return 1
    return 0

for ro in range(int(input())):
    V, E = map(int,input().split())
    route = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

    for i in range(E):
        start, end = map(int,input().split())
        route[start][end] = 1
    # print(route)

    start_node, goal_node = map(int,input().split())

    print('#%d %d' %(ro + 1, dfs(start_node,goal_node)))
