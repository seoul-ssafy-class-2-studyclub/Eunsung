poss_dir = [0, [(1, 0), (1, 1)], [(0, 1), (1, 1)], [(1, 0), (0, 1), (1, 1)] ]

nxt_dir = {
    (1, 0): 1,
    (0, 1): 2,
    (1, 1): 3,
}

def find_route(y, x, d):
    global cnt

    res = 0

    if (y, x) == (N - 1, N - 1):
        
        return 1
    
    if cache[d].get((y, x)) != None:
        return cache[d][(y, x)]
    
    
    for dx, dy in poss_dir[d]:
        if dx:
            if not x + dx < N or board[y][x + dx]:
                continue
        if dy:
            if not y + dy < N or board[y + dy][x]:
                continue

        ry = y + dy
        rx = x + dx
        flag = 0
        if not board[ry][rx]:
            res += find_route(ry, rx, nxt_dir[(dx, dy)])
    
    cache[d][(y, x)] = res
    return res


N = int(input())
board = []
for y in range(N):
    board.append(list(map(int,input().split())))

cnt = 0
cache = [{} for _ in range(4)]

print(find_route(0, 1, 1))