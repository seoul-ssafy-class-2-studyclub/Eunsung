from collections import deque

near = [(0, 1), (0, -1), (1, 0), (-1, 0)]

H, W = map(int,input().split())


board = [0] * H
exits = [[False] * W for _ in range(H)]
jihun = []
fire = []
for y in range(H):
    board[y] = list(input())
    for x in range(W):
        if board[y][x] == 'J':
            jihun = [(y, x, 0)]
        elif board[y][x] == 'F':
            fire.append((y, x))
        
        if board[y][x] in  ['.', 'J'] and (not y or y == H - 1 or not x or x == W - 1):
            exits[y][x] = True

jihun = deque(jihun)
# print(jihun)
fire = deque(fire)
flag = 0

while jihun:
    firelength = len(fire)
    for _ in range(firelength):
        fy, fx = fire.popleft()

        for dy, dx in near:
            rfy = fy + dy
            rfx = fx + dx
            if 0 <= rfy < H and 0 <= rfx < W and board[rfy][rfx] in ['.', 'J']:
                board[rfy][rfx] = 'F'
                fire.append((rfy, rfx))
    
    jihunlength = len(jihun)
    for _ in range(jihunlength):
        jy, jx, cnt = jihun.popleft()
        if exits[jy][jx]:
            flag = 1
            break

        for dy, dx in near:
            rjy = jy + dy
            rjx = jx + dx
            if 0 <= rjy < H and 0 <= rjx < W and board[rjy][rjx] == '.':
                board[rjy][rjx] = 'J'
                jihun.append((rjy, rjx, cnt + 1))
        
    if flag:
        break

if flag:
    print(cnt + 1)

else:
    print('IMPOSSIBLE')
