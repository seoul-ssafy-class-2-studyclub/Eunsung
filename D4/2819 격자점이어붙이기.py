near = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(y, x, res):
    global cnt

    if len(res) == 7:
        if maked.get(res) == None:
            cnt += 1
            maked[res] = 1
        return
    
    for dy, dx in near:
        ry = y + dy
        rx = x + dx
        if 0 <= ry < 4 and 0 <= rx < 4:
            dfs(ry, rx, res + board[ry][rx])


for ro in range(int(input())):
    board = [0] * 4
    for y in range(4):
        board[y] = list(map(str,input().split()))
    
    maked = dict()
    cnt = 0
    for y in range(4):
        for x in range(4):
            dfs(y, x, board[y][x])
    print('#%d %d' %(ro + 1, cnt))