dydx = [(y, x) for y in range(-1,2) for x in range(-1,2) if x != 0 or y != 0]

def make_board(size):
    board = []
    for i in range(size):
        board.append([0] * size)
    board[size // 2- 1][size // 2 - 1] = 2
    board[size // 2][size // 2] = 2
    board[size // 2][size // 2 - 1] = 1
    board[size // 2- 1][size // 2] = 1
    return board

def change_board(start_y, start_x, dy, dx, color):
    change_list = []
    while 0 <= start_y + dy < size and 0 <= start_x + dx < size:
        start_y, start_x = start_y + dy, start_x + dx

        check = board[start_y][start_x]

        if not check:
            break
        
        if check != color:
            change_list.append((start_y, start_x))
        
        if check == color:
            return change_list
    return []

def oselo(y, x, color):
    change = []
    for dy, dx in dydx:
        change += change_board(y, x, dy, dx, color)
    for change_y, change_x in change:
        board[change_y][change_x] = color
    return board

result = []
for game in range(int(input())):
    size, rounds = map(int,input().split())

    board = make_board(size)

    for round in range(rounds):
        x, y, color = map(int,input().split())
        y -= 1
        x -= 1
        board[y][x] = color
        board = oselo(y, x, color)

    white_c = 0
    black_c = 0

    for i in range(size):
        for l in range(size):
            if board[i][l] == 1:
                white_c += 1 
            elif board[i][l] == 2:
                black_c += 1
        
    result.append(f'#{game + 1} {white_c} {black_c}')

for value in result:
    print(value)