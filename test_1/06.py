def solution(board, r, c):
    answer = 0

    ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dp = {}

    total = 0
    for y in range(4):
        for x in range(4):
            if board[y][x]:
                total |= 1 << board[y][x]
    print(total)

    def ctl_move(y, x, d):
        
        ny, nx = y, x
        dy, dx = ds[d]
        while True:
            if d == 1:
                if ny == 0 or board[ny][nx]:
                    return ny, nx
                else 


    return answer

print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 1, 0))