def dfs(start, n, result, visited):
    if n == N - 1:
        result += board[n][start]
        return result

    res = 9 * N
    for i in visited:
        res = min(res, dfs(i, n + 1, result+board[n][start],visited - {i}))
    
    return res    

for ro in range(int(input())):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int,input().split())))

    result = 9 * N
    for j in range(N):
        temp = dfs(j, 0, 0, set(range(N)) - {j})
        if result > temp:
            result = temp
    print('#%d %d' %(ro + 1, result))
    