for rounds in range(1, int(input())+1):
    N, M = map(int,input().split())

    board = []

    for i in range(N+1):
        board.append([0]*(N+1))
    for i in range(M):
        y, x = map(int,input().split())

        board[y][x] = 1
        board[x][y] = 1

    count = 0
    for x in range(N+1):
        for y in range(N+1):
            if y != x:
                for z in range(N+1):
                    if z != x and z != y:
                        if board[y][x] == 1 and board[y][z] ==1 and board[z][x] ==1:
                            count += 1
    print(f'#{rounds} {int(count/6)}')
