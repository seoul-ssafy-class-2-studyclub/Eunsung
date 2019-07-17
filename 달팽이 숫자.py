#보드를 0으로 초기화
import math
import copy

for rounds in range(int(input())):

    size = int(input())
    board = []
    row = []

    for i in range(size):
        row.append(0)
    for i in range(size):
        board.append(copy.deepcopy(row))

    num = 1
    curve = 0 # 0<=curve<=2*(n-1)
    x = -1
    y = 0
    
    for l in range(size):
        x += 1
        board[y][x] = num
        num += 1
    curve += 1
    
    while num <= size **2:
        if curve % 4 == 1 :
            for f in range(size-math.ceil(curve / 2)):
                y += 1
                board[y][x] = num
                num += 1
            curve += 1

        elif curve % 4 == 2 :
            for f in range(size-math.ceil(curve / 2)):
                x -= 1
                board[y][x] = num
                num += 1
            curve += 1

        elif curve % 4 == 3 :
            for f in range(size-math.ceil(curve / 2)):
                y -= 1
                board[y][x] = num
                num += 1
            curve += 1

        elif curve % 4 == 0 :
            for f in range(size-math.ceil(curve / 2)):
                x += 1
                board[y][x] = num
                num += 1
            curve += 1

    for i in range(size):
        board[i] = list(map(str,board[i]))

    print(f'#{rounds + 1}')
    for i in range(size):
        print(' '.join(board[i]))