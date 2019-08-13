import sys
sys.stdin = open('input.txt', 'r')

def check(board):
    for M in range(100, 0, -1):
        if not M % 2:
            for y in range(100):
                for x in range(M // 2 - 1, 100 - M // 2):
                    if board[y][x] == board[y][x+1]:
                        for i in range(1, M // 2):
                            if board[y][x-i] != board[y][x + 1 + i]:
                                break
                            elif i == M // 2 - 1:
                                return M
                    
                    if board[x][y] == board[x+1][y]:
                        for i in range(1, M // 2):
                            if board[x - i][y] != board[x+ 1+ i][y]:
                                break
                            elif i == M // 2 - 1:
                                return M
        
        elif M % 2:
            for y in range(100):
                for x in range(M // 2 - 1, 100 - M // 2 - 1):
                    if board[y][x] == board[y][x+2]:
                        for i in range(1, M // 2):
                            if board[y][x-i] != board[y][x + 2 + i]:
                                break
                            elif i == M // 2 - 1:
                                return M
                    
                    if board[x][y] == board[x+2][y]:
                        for i in range(1, M // 2):
                            if board[x - i][y] != board[x+ 2+ i][y]:
                                break
                            elif i == M // 2 - 1:
                                return M    

for round in range(10):
    ro = input()
    board = []
    for i in range(100):
        board.append(input())

    
            
    print('#%d %s' %(round + 1, check(board)))
