def make_board(size):
    board = []
    for i in range(size):
        board.append([0] * size)
    board[size // 2- 1][size // 2 - 1] = 2
    board[size // 2][size // 2] = 2
    board[size // 2][size // 2 - 1] = 1
    board[size // 2- 1][size // 2] = 1
    return board

size, rounds = map(int,input().split())

board = make_board(size)

for round in range(rounds):
    y, x, color = map(int,input().split())
    y -= 1
    x -= 1
    board[x][y] = color






for i in range(size):
    print(''.join(list(map(str,board[i]))))