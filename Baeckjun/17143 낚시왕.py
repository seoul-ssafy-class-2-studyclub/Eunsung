directions = {1:(-1, 0), 2:(1, 0), 3:(0, 1), 4:(0, -1), }
aside = {1:2, 2:1, 3:4, 4:3, }
import sys

def move(fish):
    r, c, s, d, z = fish
    dr, dc = directions[d]
    
    if dr:
        r += s * dr
        r = r % (2 * (R - 1))
        if r < 1:
            r = 2 - r
            d = aside[d]
        if r > R:
            r = 2 * R - r
            d = aside[d]
    
    elif dc:
        c += s * dc
        c = c % (2 * (C - 1))
        if c < 1:
            c = 2 - c
            d = aside[d]
        if c > C:
            c = 2 * C - c
            d = aside[d]
    
    board[r][c].append(z)
    if len(board[r][c]) > 1:
        cache.append((r,c))
    queue.append([r, c, s, d, z])

    return [r, c, s, d, z]

R, C, M = map(int,sys.stdin.readline().split())
queue = []
catched_fish = 0
board = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
cache = []

for _ in range(M):
    r, c, s, d, z = map(int,sys.stdin.readline().split())
    board[r][c].append(z)
    queue.append([r,c,s,d,z])

for x in range(1, C + 1):

    for depth in range(1, R + 1):
        if board[depth][x]:
            catched_fish += board[depth][x].pop(0)
            break
    
    for _ in range(len(queue)):
        r, c, s, d, z = queue.pop(0)
        if not board[r][c] or board[r][c][0] != z:
            continue
        board[r][c].pop(0)
        now_fish = move([r, c, s, d, z])
        

    for _ in range(len(cache)):
        x, y = cache.pop()
        if len(board[x][y]) > 1:
            board[x][y] = [max(board[x][y])]

print(catched_fish)
