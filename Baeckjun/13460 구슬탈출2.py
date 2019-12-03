directions = [(-1, 0, -1), (0, 1, +2), (1, 0, +1), (0, -1, -2)]
from pprint import pprint
from copy import deepcopy

def move(d, red, blue, now_board, cnt):
    global min_cnt
    board = deepcopy(now_board)
    if cnt == 11 or cnt >= min_cnt:
        return 

    balls = [red, blue]
    direction = directions[d]
    balls.sort(key=lambda x: x[abs(direction[2])] * direction[2], reverse=True)
    
    dy = direction[0]
    dx = direction[1]
    hallin = []
    for idx in range(len(balls)):
        y = balls[idx][1]
        x = balls[idx][2]
        board[y][x] = '.'
        y += dy
        x += dx
        while board[y][x] == '.':
            y += dy
            x += dx
        if board[y][x] == 'O':
            # board[ball[1]][ball[2]] = '.'
            hallin.append(balls[idx][0])

        if board[y][x] in ['#', 'B', 'R']:
            y -= dy
            x -= dx
            balls[idx] = (balls[idx][0], y, x)
            board[y][x] = balls[idx][0]
    if 'B' in hallin:
        return
    if 'R' in hallin:
        if min_cnt > cnt:
            min_cnt = cnt
        return
    if balls[0][0] == 'R':
        red = balls[0]
        blue = balls[1]
    else:
        red = balls[1]
        blue = balls[0]
    for di in range(4):
        if d % 2 == di % 2:
            continue 
        move(di, red, blue, board, cnt + 1)

N, M = map(int,input().split())
g_board = [0] * N
red = (0, 0)
blue = (0, 0)
hole = (0, 0)
min_cnt = 11
min_curve = 11
visited = [[False] * M for _ in range(N)]
for y in range(N):
    g_board[y] = list(input())
    for x in range(M):
        if g_board[y][x] == 'R':
            red = ('R', y, x)
        elif g_board[y][x] == 'B':
            blue = ('B', y, x)
        elif g_board[y][x] == 'O':
            hole = (y, x)
for d in range(4):
    move(d, red, blue, g_board, 1)

if min_cnt == 11:
    min_cnt = -1
print(min_cnt)
    
        
