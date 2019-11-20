# horses = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
horses = [(1, 2), (1, -2), (-1, 2), (2, 1), (2, -1), (-2, 1)]
monkeys = [(1, 0), (-1, 0), (0, -1), (0, 1)]
# monkeys = [(1, 0), (0, 1)]

def dfs(y, x, k, cnt):
    global min_cnt
    if (y, x) == (H - 1, W - 1):
        if cnt < min_cnt:
            min_cnt = cnt
        return

    if dp[y * W + x][0] <= k:
        if dp[y * W + x][1] <= cnt:
            return
    
    if cnt >= min_cnt:
        return
    
    tk, tc = dp[y * W + x] if dp[y * W + x][0]
    dp[y * W + x] = (mindp, cnt)

    if k < K:
        for dy, dx in horses:
            ry = y + dy
            rx = x + dx
            if 0 <= ry < H and 0 <= rx < W and not board[ry][rx]:
                # print(y, dy, ry, '//', x, dx, rx)
                dfs(ry, rx, k + 1, cnt + 1)
    
    for dy, dx in monkeys:
        ry = y + dy
        rx = x + dx
        if 0 <= ry < H and 0 <= rx < W and not board[ry][rx]:
            dfs(ry, rx, k, cnt + 1)
        

K = int(input())
H, W = map(int,input().split())

board = [0] * H
walls = []
min_cnt = 4000
for y in range(H):
    board[y] = list(map(int,input().split()))
    for x in range(W):
        if board[y][x] == 1:
            walls.append((y, x))
dp = [(K, 4000)] * (W * H + 1)
# dp = 

dfs(0,0,0,0)
if min_cnt == 4000:
    min_cnt = -1

print(min_cnt)