def replace():
    idx = 1
    y, x, dis = exists[1]
    res = (y, x, dis)
    max_len = len(exists)
    if max_len > 2:
        exists[1] = exists.pop()
    else:
        exists.pop()
    max_len -= 1
    
    while True:
        nxt1 = idx * 2
        nxt2 = idx * 2 + 1
        if nxt1 < max_len:
            if exists[idx][2] > exists[nxt1][2]:
                if nxt2 < max_len and exists[idx][2] > exists[nxt2][2]:
                    min_idx = nxt1 if exists[nxt1][2] < exists[nxt2][2] else nxt2
                    exists[idx], exists[min_idx] = exists[min_idx], exists[idx]
                    idx = min_idx
                    continue
                
                else:
                    exists[idx], exists[nxt1] = exists[nxt1], exists[idx]
                    idx = nxt1
                    continue

            else:
                if nxt2 < max_len:
                    if exists[idx][2] > exists[nxt2][2]:
                        exists[idx], exists[nxt2] = exists[nxt2], exists[idx]
                        idx = nxt2
                        continue
                    else:
                        break
                else:
                    break
        else:
            break
    return res 

def createnode(y, x, dis):
    exists.append((y, x, dis))
    idx = len(exists) - 1
    while idx > 1 and exists[idx // 2][2] > exists[idx][2]:
        exists[idx // 2], exists[idx] = exists[idx], exists[idx // 2]
        idx = idx // 2

dys = [1, -1, 0, 0]
dxs = [0, 0, -1, 1]

for ro in range(int(input())):
    N = int(input())
    board = [0] * N
    dist = [[99999] * N for _ in range(N)]
    dist[0][0] = 0
    exists = [0, (0, 0, 0)]
    visited = [[False] * N for _ in range(N)]

    for y in range(N):
        board[y] = list(map(int,input().split()))
    
    while True:
        if visited[N - 1][N - 1]:
            break
        
        min_y, min_x, dis = replace()
        visited[min_y][min_x] = True

        for i in range(4):
            dy = dys[i]
            dx = dxs[i]
            ry = min_y + dy
            rx = min_x + dx
            if not (0 <= ry < N and 0 <= rx < N):
                continue

            gap = board[ry][rx] - board[min_y][min_x] + 1 if board[ry][rx] - board[min_y][min_x] > 0 else 1
            if not visited[ry][rx] and dist[ry][rx] > dis + gap:
                dist[ry][rx] = gap + dis
                createnode(ry, rx, dist[ry][rx])
    
    print('#%d %d' %(ro + 1, dist[N - 1][N - 1]))