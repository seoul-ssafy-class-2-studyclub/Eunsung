from collections import deque
near = [(1, 0), (-1, 0), (0, 1), (0, -1)]


N, M = map(int, input().split())

board = [0] * N
for y in range(N):
    board[y] = input()
    for x in range(M):
        if board[y][x] == '0':
            start = (y, x)


queue = deque()
save = [(start, 0, 0)]
flag = 0
result = 2501
while save:
    visited = [[False] * M for _ in range(N)] 
    queue.append(save.pop(0))
    while queue:
        now, status, cnt = queue.popleft()
        if cnt >= result:
            break
        # print(now)
        y = now[0]
        x = now[1]
        if board[y][x] == '1':
            if result > cnt:
                result = cnt
            flag = 1
            break
        for dy, dx in near:
            ry = y + dy
            rx = x + dx
            if 0 <= ry < N and 0 <= rx < M and not visited[ry][rx]:
                visited[ry][rx] = True
                if board[ry][rx] in ['.', '0', '1']:
                    queue.append(((ry, rx), status, cnt + 1))
                # if 'a' <= board[ry][rx] <= 'z' and not status & (1 << (ord(board[ry][rx]) - ord('a'))):
                if 'a' <= board[ry][rx] <= 'z':
                    # queue.append(((ry, rx), status | (1 << (ord(board[ry][rx]) - ord('a'))), cnt + 1, 1 << (N * ry + rx)))
                    save.append(((ry, rx), status | (1 << (ord(board[ry][rx]) - ord('a'))), cnt + 1))
                if 'A' <= board[ry][rx] <= 'Z':
                    if status & (1 << (ord(board[ry][rx]) - ord('A'))):
                        queue.append(((ry, rx), status, cnt + 1))
    # print('ddd')
    # if flag:
    #     break
if not flag:
    result = -1
print(result)