directions = {
    1:[(0,-1), (0, 1), (-1,0), (1, 0)],
    2:[(0,-1), (0, 1)],
    3:[(-1,0), (1, 0)],
    4:[(0,-1), (1, 0)],
    5:[(0, 1), (1, 0)],
    6:[(0, 1), (-1,0)],
    7:[(0,-1), (-1,0),]
}
aside ={
    (0, -1): (0, 1),
    (0, 1): (0, -1),
    (-1, 0): (1, 0),
    (1, 0): (-1, 0),
}

for ro in range(int(input())):
    N, M, R, C, L = map(int,input().split())
    board =[]
    for _ in range(N):
        board.append(list(map(int,input().split())))
    visited = [[False] * M for _ in range(N)]
    
    queue = [(R, C)]
    visited[R][C] = True
    cnt = 0
    for _ in range(L):
        # print(queue)
        for _ in range(len(queue)):
            temp = queue.pop(0)
            cnt += 1
            y, x = temp

            for dx, dy in directions[board[y][x]]:
                # print(dy, dx)
                ry = y + dy
                rx = x + dx
                if 0 <= ry < N and 0 <= rx < M:
                    if board[ry][rx] and aside[(dx, dy)] in directions[board[ry][rx]] and not visited[ry][rx]:
                        visited[ry][rx]  = True
                        queue.append((ry, rx))
                        # print(ry, rx)
    
    print('#%d %d' %(ro + 1, cnt))
        
