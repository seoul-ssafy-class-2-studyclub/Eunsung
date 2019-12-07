near = [(1, 0), (-1, 0), (0, 1), (0, -1)]

from collections import deque

H, W, T = map(int,input().split())

board = [0] * H

gram = (0, 0)
for y in range(H):
    board[y] = list(map(int,input().split()))
    for x in range(W):
        if board[y][x] == 2:
            gram = (y, x)
visited = [[False] * W for _ in range(H)]

result = 'Fail'
queue = deque()
if gram == (0, 0) and H + W - 2 <= T:
    result = H + W - 2
goal = H + W - 2
ifgram = 99999
gramflag = 0
queue.append((0, 0, 0))
while queue and gram != (0, 0) and not gramflag:
    y, x, cnt = queue.popleft()

    if cnt > T:
        result = 'Fail'
        break

    if (y, x) == (H - 1, W - 1):
        result = cnt
        break

    for dy, dx in near:
        ry = y + dy
        rx = x + dx

        if 0 <= ry < H and 0 <= rx < W and board[ry][rx] != 1 and not visited[ry][rx]:
            visited[ry][rx] = True
            if board[ry][rx] == 2 and cnt + 1 + goal - (ry + rx) <= T:
                ifgram = cnt + goal - (ry + rx) + 1
                gramflag = 1
                break
            else:
                queue.append((ry, rx, cnt + 1))

if ifgram != 99999:
    if type(result) != str:
        result = min(ifgram, result)
    else:
        result = ifgram

print(result)