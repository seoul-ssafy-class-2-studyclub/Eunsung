from collections import deque

near = [(1, 0), (-1, 0), (0, 1), (0, -1)]


M, N = map(int,input().split())
board = [0] * N
tomatos = deque()
total = N * M
for y in range(N):
    board[y] = list(map(int,input().split()))

    for x in range(M):

        if board[y][x] == 1:
            tomatos.append((y, x))
            total -= 1
        if board[y][x] == -1:
            total -= 1
cnt = 0
while tomatos:
    for _ in range(len(tomatos)):
        y, x = tomatos.popleft()

        for dy, dx in near:
            ry = y + dy
            rx = x + dx

            if 0 <= ry < N and 0 <= rx < M:
                if board[ry][rx] == 0:
                    board[ry][rx] = 1
                    total -= 1
                    tomatos.append((ry, rx))
    cnt += 1

if total:
    cnt = 0

print(cnt - 1)
