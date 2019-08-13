import sys
sys.stdin = open('input.txt', 'r')

for round in range(10):
    M = int(input())
    board = []
    for i in range(8):
        board.append(input())
    count = 0
    if not M % 2:
        for y in range(8):
            for x in range(M // 2 - 1, 8 - M // 2):
                if board[y][x] == board[y][x+1]:
                    for i in range(1, M // 2):
                        if board[y][x-i] != board[y][x + 1 + i]:
                            break
                        elif i == M // 2 - 1:
                            count += 1
                
                if board[x][y] == board[x+1][y]:
                    for i in range(1, M // 2):
                        if board[x - i][y] != board[x+ 1+ i][y]:
                            break
                        elif i == M // 2 - 1:
                            count += 1
    elif M == 3:
        for y in range(8):
            for x in range(M // 2 - 1, 8 - M // 2 - 1):
                if board[y][x] == board[y][x+2]:
                    count += 1
            
                if board[x][y] == board[x+2][y]:
                    count += 1



    elif M % 2:
        for y in range(8):
            for x in range(M // 2 - 1, 8 - M // 2 - 1):
                if board[y][x] == board[y][x+2]:
                    for i in range(1, M // 2):
                        if board[y][x-i] != board[y][x + 2 + i]:
                            break
                        elif i == M // 2 - 1:
                            count += 1
                
                if board[x][y] == board[x+2][y]:
                    for i in range(1, M // 2):
                        if board[x - i][y] != board[x+ 2+ i][y]:
                            break
                        elif i == M // 2 - 1:
                            count += 1
        
    print('#%d %s' %(round + 1, count))
