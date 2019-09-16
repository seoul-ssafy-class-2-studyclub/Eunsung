def combi(arr, now):
    global max_pos

    if len(arr) == N:
        
        if now * 100 > max_pos:
            max_pos = now * 100

        return

    for i in range(N):
        if visited[i] or now * board[len(arr)][i] * 100 <= max_pos:
            continue
        visited[i] = True
        combi(arr + [i], now * board[len(arr)][i])
        visited[i] = False


for ro in range(int(input())):
    N = int(input())
    board = []
    for y in range(N):
        board.append(list(map(float,input().split())))
        for x in range(N):
            board[y][x] = board[y][x] / 100
    
    visited = [False for _ in range(N)]
    max_pos = 0

    temp = []

    combi([], 1)
    print('#%d %f' %(ro + 1, max_pos))

