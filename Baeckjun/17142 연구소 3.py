near = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def combinations(arr, i):
    global min_time

    if len(arr) == M:
        cnt = 0
        t = 0
        flag = 0
        visited = [[False] * N for _ in range(N)]
        while arr:
            if cnt == total_zero:
                flag = 1
                break
            t += 1

            for y, x in arr:
                visited[y][x] = True

            for _ in range(len(arr)):
                y, x = arr.pop(0)
                for dx, dy in near:
                    ry = y + dy
                    rx = x + dx
                    if 0 <= ry < N and 0 <= rx < N:
                        if not board[ry][rx] and not visited[ry][rx]:
                            visited[ry][rx] = True
                            arr.append((ry, rx))
                            cnt += 1
                        if board[ry][rx] == 2 and not visited[ry][rx]:
                            visited[ry][rx] = True
                            arr.append((ry, rx))
        if flag:
            if min_time > t:
                min_time = t
                return


    for idx in range(i + 1, len(virus)):
        combinations(arr + [virus[idx]], idx)

N, M = map(int,input().split())

board = []
virus = []
total_zero = 0
for y in range(N):
    board.append(list(map(int,input().split())))
    for x in range(N):
        if board[y][x] == 2:
            virus.append((y, x))
        if not board[y][x]:
            total_zero += 1
min_time = 9999
combinations([], -1)

if min_time == 9999:
    min_time = -1
print(min_time)

