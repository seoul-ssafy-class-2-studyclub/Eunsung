def daching(board_180):
    board_180.reverse()
    for i in range(N):
        board_180[i].reverse()
    return board_180

def re90(board_90):
    board_90 = list(map(list,zip(*board_90)))
    for idx in range(len(board_90)):
        board_90[idx].reverse()
    return board_90

def re270(board_270):
    board_270 = re90(board_270)
    board_270 = daching(board_270)
    return board_270

def no(board):
    return board

directions = {'up':[no, no], 'left':[re90, re270], 'right':[re270, re90], 'down':[daching, daching]}


def play(di):
    global board

    board = directions[di][0](board)
    
    for y in range(1, N):
        for x in range(N):
            if board[y][x]:
                dy = -1
                while 0 < y + dy < N and not board[y + dy][x]:
                    dy -= 1
                if board[y + dy][x] == board[y][x] and not visited[y + dy][x]:
                    temp = board[y][x]
                    board[y][x] = 0
                    board[y + dy][x] += temp
                    visited[y + dy][x] = True
                    
                elif board[y + dy][x] == 0:
                    temp = board[y][x]
                    board[y][x] = 0
                    board[y + dy][x] += temp
                    
                else:
                    temp = board[y][x]
                    board[y][x] = 0
                    board[y + dy + 1][x] += temp
                    
    board = directions[di][1](board)

    return board

for ro in range(int(input())):
    N, di = input().split()
    N = int(N)
    board = []
    visited = [[False] * N for _ in range(N)]
    for _ in range(N):
        board.append(list(map(int,input().split())))

    print('#%d' %(ro + 1))


    board = play(di)
    for line in board:
        for val in line:
            print(val, end=' ')
        print()
