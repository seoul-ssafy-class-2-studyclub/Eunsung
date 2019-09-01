diretions = {1: (0, -1), 2:(0, 1), 3:(-1, 0), 4:(1, 0)}
aside = {1:2, 2:1, 3:4, 4:3}

def move(y, x, z, d):
    dx, dy = diretions[d]
    ry = y + dy
    rx = x + dx
    if ry == 0 or ry == N -1 or rx == 0 or rx == N -1:
        z = z // 2
        d = aside[d]

    return (ry, rx, z, d) 

for ro in range(int(input())):
    N, M, K = map(int,input().split())

    board = [[[] for _ in range(N)] for _ in range(N)]
    queue = []
    temp = []

    for _ in range(K):
        y, x, z, d = map(int,input().split())
        queue.append((y, x, z, d))
        board[y][x].append((z, d))
    
    for time in range(M):
        for _ in range(len(queue)):
            y, x, z, d = queue.pop(0)
            if not board[y][x] or board[y][x][0] != (z, d):
                continue
            board[y][x].pop(0)
            y, x, z, d = move(y, x, z, d)
            if z == 0:
                continue
            board[y][x].append((z, d))

            if len(board[y][x]) > 1:
                temp.append((y, x))
            queue.append((y, x, z, d))
        
        for _ in range(len(temp)):
            y, x = temp.pop()
            if len(board[y][x]) == 1:
                continue
            temp_sum = 0
            max_z = 0
            for z, d in board[y][x]:
                temp_sum += z
                if z > max_z:
                    max_z = z
                    now_d = d
            board[y][x] = [(temp_sum, now_d)]
            queue.insert(0, (y, x, temp_sum, now_d))
    
    sums = 0
    for y in range(N):
        for x in range(N):
            if board[y][x]:
                sums += board[y][x][0][0]
    print('#%d %d' %(ro + 1,sums))
