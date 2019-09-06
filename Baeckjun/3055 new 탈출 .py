near = [(-1, 0), (1, 0), (0, -1), (0, 1)]

R, C = map(int,input().split())
board = []
waters = []
visited = [[False] * C for _ in range(R)]
for y in range(R):
    board.append(list(input()))
    for x in range(C):
        if board[y][x] == '*':
            waters.append((y, x, 1))
        elif board[y][x] == 'S':
            start = (y, x)
        elif board[y][x] == 'D':
            goal = (y, x)
res = -1

while waters:
    for _ in range(len(waters)):
        y, x, t = waters.pop(0)
        board[y][x] = t - 1
        for dx, dy in near:
            ry = y + dy
            rx = x + dx
            if 0 <= ry < R and 0 <= rx < C:
                if board[ry][rx] == '.' or board[ry][rx] == 'S':
                    waters.append((ry, rx, t + 1))
                    board[ry][rx] = t
s_queue = [(start, 1)]
visited[start[0]][start[1]] = True
while s_queue:

    for _ in range(len(s_queue)):
        (y, x), now = s_queue.pop(0)
        

        for dx, dy in near:
            ry = y + dy
            rx = x + dx
            if 0 <= ry < R and 0 <= rx < C:
                if visited[ry][rx]:
                    continue

                if board[ry][rx] == 'D':
                    res = now
                    break

                if board[ry][rx] in ['.', 'S'] or (board[ry][rx] != 'X' and board[ry][rx] > now):
                    visited[ry][rx] = True
                    s_queue.append(((ry, rx), now + 1))
                
    if res != -1:
        break


if res == -1:   
    res = 'KAKTUS'
print(res)
