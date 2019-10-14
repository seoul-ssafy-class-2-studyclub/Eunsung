near = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def countingroom(y, x, roomnumber):
    global rooms
    visited[y][x] = True
    for idx in range(4):
        if board[y][x] & (1 << idx):
            
            continue
        dy, dx = near[idx]
        ry = y + dy
        rx = x + dx
        if 0 <= ry < M and 0 <= rx < N and not visited[ry][rx]:
            size_of_rooms[roomnumber] += 1
            countingroom(ry, rx, roomnumber)


N, M = map(int,input().split())
board = [0] * M
visited = [[False] * N for _ in range(M)]
for y in range(M):
    board[y] = list(map(int,input().split()))

rooms = 0
cache = []
neighbor = []
size_of_rooms = [0] * 2501

for y in range(M):
    for x in range(N):
        if visited[y][x]:
            continue
        rooms += 1
        size_of_rooms[rooms] += 1
        countingroom(y, x, rooms)


print(rooms)
print(size_of_rooms[:rooms + 1])
# print(neighbor)