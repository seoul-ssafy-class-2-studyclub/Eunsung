near = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 1)]

def movemaze():
    walls[7] = []
    for y in range(N - 2, -1, -1):
        for _ in range(len(walls[y])):
            x = walls[y].pop(0)
            board[y][x] = '.'
            board[y + 1][x] = '#'
            walls[y + 1].append(x)
    

N = 8
board = [0] * N
walls = [[] for _ in range(N)]
for y in range(N):
    board[y] = list(input())
    for x in range(N):
        if board[y][x] == '#':
            walls[y].append(x)
start = (7, 0)

queue = [start]
result = 0
while queue:
    for _ in range(len(queue)):
        y, x = queue.pop(0)
        cnt = 0
        for up_y in range(y):
            cnt += len(walls[up_y])
        if cnt == 0:
            result = 1
            break

        for dy, dx in near:
            ry = y + dy
            rx = x + dx
            if ry == 0 and rx == 7:
                result = 1
                break

            if 0 <= ry < N and 0 <= rx < N and (0 < ry and board[ry - 1][rx] != '#') and board[ry][rx] != '#':
                queue.append((ry, rx))
    movemaze()
    if result != 0:
        break

print(result)
