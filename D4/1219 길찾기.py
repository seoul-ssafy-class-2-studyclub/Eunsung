def navigator(y,board,crosspoint):
    if board[y][99]:
        return 1
    
    for i in range(99):
        if board[y][i]:
            crosspoint.append(y)
            board[y][i] = False
            return navigator(i,board,crosspoint)
    
    x = crosspoint.pop()

    if not crosspoint:
        return 0

    return navigator(x,board,crosspoint)



for rounds in range(1,11):
    tc, N = map(int,input().split())

    roads = list(map(int,input().split()))
    road_yx = []

    for i in range(len(roads) // 2):
        road_yx.append((roads[2*i], roads[2*i + 1]))
    
    board = [[False for _ in range(100)] for _ in range(100)]
    for (y,x) in road_yx:
        board[y][x] = True

    print(f'#{tc} {navigator(0,board,[])}')
