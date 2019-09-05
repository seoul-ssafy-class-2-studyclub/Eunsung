def findroute(arr, y, x, delta):
    if delta in [(-1, 1), (1, 1)] and (y + 1, x - 1) == start:
        return len(arr)

    res = -1
    if delta == (-1, 1):
        ry = y + 1
        rx = x - 1
        if 0 <= ry < N and 0 <= rx < N:
            if not board[ry][rx] in arr:
                res = max(res, findroute(arr + [board[ry][rx]], ry, rx, (-1, 1)))
        

    else:    
        for dx, dy in [delta, directions[delta]]:
            ry = y + dy
            rx = x + dx
            if 0 <= ry < N and 0 <= rx < N:
                if not board[ry][rx] in arr:
                    res = max(res, findroute(arr + [board[ry][rx]], ry, rx, (dx, dy)))
        
    return res

    

directions = {
    (-1, -1): (1, -1),
    (1, -1): (1, 1),
    (1, 1): (-1, 1),
}


for ro in range(int(input())):
    N = int(input())
    board = []
    for y in range(N):
        board.append(list(map(int,input().split())))
    result = -1
    for y in range(N):
        for x in range(N):
            start = (y, x)
            result = max(result, findroute([board[y][x]], y, x, (-1, -1)))
    # result = max(result, findroute([board[2][1]], 2, 1, (-1, -1)))
    print('#%d %d' %(ro + 1, result))

    
    
