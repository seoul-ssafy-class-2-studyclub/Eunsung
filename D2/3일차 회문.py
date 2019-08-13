for round in range(int(input())):
    N, M = map(int,input().split())
    board = []
    for i in range(N):
        board.append(input())
    result = ''
    if not M % 2:
        for y in range(N):
            for x in range(M // 2 - 1, N - M // 2):
                if board[y][x] == board[y][x+1]:
                    for i in range(1, M // 2):
                        if board[y][x-i] != board[y][x + 1 + i]:
                            break
                        elif i == M // 2 - 1:
                            result = board[y][x - M // 2 + 1 : x + M // 2 + 1 ]
                
                if board[x][y] == board[x+1][y]:
                    for i in range(1, M // 2):
                        if board[x - i][y] != board[x+ 1+ i][y]:
                            break
                        elif i == M // 2 - 1:
                            result = ''
                            for k in range(x  - M // 2 + 1, x + M // 2 + 1):
                                result += board[k][y]
    
    elif M % 2:
        for y in range(N):
            for x in range(M // 2 - 1, N - M // 2):
                if board[y][x] == board[y][x+2]:
                    for i in range(1, M // 2):
                        if board[y][x-i] != board[y][x + 2 + i]:
                            break
                        elif i == M // 2 - 1:
                            result = board[y][x - M // 2 + 1 : x + M // 2 + 2 ]
                
                if board[x][y] == board[x+2][y]:
                    for i in range(1, M // 2):
                        if board[x - i][y] != board[x+ 2+ i][y]:
                            break
                        elif i == M // 2 - 1:
                            result = ''
                            for k in range(x  - M // 2 + 1, x + M // 2 + 2):
                                result += board[k][y]    
        
    print('#%d %s' %(round + 1, result))
