D = {
    1:[[(0,1)], [(0,-1)], [(1,0)], [(-1,0)]],
    2:[[(1,0), (-1,0)], [(0,1), (0,-1)]], 
    3:[[(1,0),(0,1)], [(0,1),(-1,0)], [(-1,0),(0,-1)], [(0,-1),(1,0)]], 
    4:[[(0,1), (0,-1), (1,0)], [(0,1), (0,-1), (-1,0)], [(0,1), (1,0), (-1,0)], [(0,-1), (1,0), (-1,0)]], 
    5:[[(0,1), (0,-1), (1,0), (-1,0)]]
}

def combi(arr, nowidx):
    if nowidx == K:
        directions_choices.append(arr)
        return
    
    now_y, now_x = cctvs[nowidx]
    for view in range(len(D[board[now_y][now_x]])):
        combi(arr + [view], nowidx + 1)

def see(cctv, d):
    global cnt
    y, x = cctv
    views = D[board[y][x]][d]

    for dx, dy in views:
        ry = y + dy
        rx = x + dx
        while 0 <= ry < N and 0 <= rx < M and board[ry][rx] < 6:
            if not board[ry][rx] and not visitied[ry][rx]:
                cnt += 1
                visitied[ry][rx] = True
            
            ry += dy
            rx += dx


N, M = map(int,input().split())
board = []
cctvs = []
directions_choices = []
zeros = 0
for y in range(N):
    board.append(list(map(int,input().split())))
    for x in range(M):
        if 1 <= board[y][x] <= 5:
            cctvs.append((y, x))
        if not board[y][x]:
            zeros += 1

K = len(cctvs)
combi([], 0)
max_count = 0
while directions_choices:
    visitied = [[False] * M for _ in range(N)]
    cases = directions_choices.pop(0)

    cnt = 0
    for cctv in range(len(cases)):
        see(cctvs[cctv], cases[cctv])
    
    temp = zeros - cnt

    if temp > max_count:
        max_count = temp
        
print(max_count)