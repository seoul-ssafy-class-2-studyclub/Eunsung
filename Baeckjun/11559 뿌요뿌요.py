near = [(1, 0), (-1, 0), (0, 1), (0 , -1)]

def dfs(y, x):
    visited[y][x] = True
    for dy, dx in near:
        ry = y + dy
        rx = x + dx
        if 0 <= ry < H and 0 <= rx < W and not visited[ry][rx]:
            if board[ry][rx] == board[y][x]:
                temp.append((ry,rx))
                dfs(ry, rx)
        
def gravity(y, x):
    dy = 1
    while y + dy < H and board[y + dy][x] == '.':
        dy += 1
    board[y][x], board[y + dy - 1][x] = board[y + dy - 1][x], board[y][x]


H, W = 12, 6
board = [0] * H

for y in range(H):
    board[y] = list(input())

chain = 0
bomb = []
while True:
    visited = [[False] * W for _ in range(H)]
    for y in range(H - 1, -1, -1):
        for x in range(W):
            if visited[y][x] or board[y][x] == '.':
                continue
            temp = [(y, x)]
            dfs(y, x)
            if len(temp) >= 4:
                bomb.append(temp)

    if not bomb:
        break
    chain += 1

    while bomb:
        puyo = bomb.pop()
        for y, x in puyo:
            board[y][x] = '.'
    
    for y in range(H - 1, -1, -1):
        for x in range(W):
            if board[y][x] != '.':
                gravity(y, x)
    

print(chain)
        