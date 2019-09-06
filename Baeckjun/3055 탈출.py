near = [(-1, 0), (1, 0), (0, -1), (0, 1)]

R, C = map(int,input().split())
board = []
waters = []
for y in range(R):
    board.append(list(input()))
    for x in range(C):
        if board[y][x] == '*':
            waters.append((y, x))
        elif board[y][x] == 'S':
            start = (y, x)
        elif board[y][x] == 'D':
            goal = (y, x)
res = -1
s_queue = [(start, 0)]
while s_queue:
    for _ in range(len(waters)):
        y, x = waters.pop(0)
        for dx, dy in near:
            ry = y + dy
            rx = x + dx
            if 0 <= ry < R and 0 <= rx < C:
                if board[ry][rx] == '.' or board[ry][rx] == 'S':
                    waters.append((ry, rx))
                    board[ry][rx] = '*'

    for _ in range(len(s_queue)):
        (y, x), now = s_queue.pop(0)

        if board[y][x] == '*':
            continue
        
        for dx, dy in near:
            ry = y + dy
            rx = x + dx
            if 0 <= ry < R and 0 <= rx < C:
                if board[ry][rx] == '.':
                    s_queue.append(((ry, rx), now + 1))
                if board[ry][rx] == 'D':
                    res = now + 1
                    break
    flag = 0
        
    if res != -1:
        break

    for dx, dy in near:
        ry = goal[0] + dy
        rx = goal[1] + dx
        if 0 <= ry < R and 0 <= rx < C:
            if board[ry][rx] != 'X' or board[ry][rx] != '*':
                flag += 1
    if not flag:
        break


if res == -1:   
    res = 'KAKTUS'
print(res)
