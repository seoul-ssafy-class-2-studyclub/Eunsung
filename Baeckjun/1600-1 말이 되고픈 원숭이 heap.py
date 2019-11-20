from heapq import heappop, heappush

horses = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
monkeys = [(1, 0), (-1, 0), (0, -1), (0, 1)]


K = int(input())
W, H = map(int,input().split())

board = [0] * H
dp = [[0] * W for _ in range(H)] 
min_cnt = 4000
for y in range(H):
    board[y] = list(map(int,input().split()))
queue = []
heappush(queue, (0,0,0,0,0))
GOAL = H + W

while queue:
    cnt, dis, y, x, k = heappop(queue)
    # if dp[y][x] & 1 << k:
    #     continue
    # dp[y][x] |= 1 << k
    # if dp[y][x].get(k) != None:
    #     if dp[y][x][k] <= cnt:
    #         continue
    # dp[y][x][k] = cnt
    if (y, x) == (H - 1, W - 1):
        min_cnt = cnt
        break
    
    if k < K:
        for dy, dx in horses:
            ry = y + dy
            rx = x + dx
            if 0 <= ry < H and 0 <= rx < W and not board[ry][rx]:
                
                if dp[ry][rx] & 1 << (k + 1):
                    continue
                # for tk in range(k, K - 1):
                dp[ry][rx] |= 1 << (k + 1)
                heappush(queue, (cnt + 1, GOAL - ry - rx, ry, rx, k + 1))
    
    for dy, dx in monkeys:
        ry = y + dy
        rx = x + dx
        if 0 <= ry < H and 0 <= rx < W and not board[ry][rx]:
                
            if dp[ry][rx] & 1 << k:
                continue
                # for tk in range(k, K - 1):
            dp[ry][rx] |= 1 << k
            heappush(queue, (cnt + 1, GOAL - ry - rx, ry, rx, k))

if min_cnt == 4000:
    min_cnt = -1

print(min_cnt)