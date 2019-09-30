near = [(0, 1), (0, -1), (1, 0), (-1, 0)]
from pprint import pprint
def dfs(y, x):
    
    if cache[y][x] != 0:
        return cache[y][x]

    for dy, dx in near:
        ry = y + dy
        rx = x + dx
        if 0 <= ry < N and 0 <= rx < N:
            if board[ry][rx] - board[y][x] == 1:
                if cache[ry][rx] != 0:
                    res = 1 + cache[ry][rx]
                    cache[y][x] = res
                    return res
                else:
                    res = 1 + dfs(ry, rx)
                    cache[y][x] = res
                    return res
    cache[y][x] = 1
    # print(cache)
    return 1

for ro in range(int(input())):
    N = int(input())
    board = [0] * N
    cache = [0] * N
    for y in range(N):
        board[y] = list(map(int,input().split()))
        cache[y] = [0] * N
    min_start = N ** 2
    max_cnt = 0
    for y in range(N):
        for x in range(N):
            temp = dfs(y, x)
            if temp >= max_cnt:
                if temp == max_cnt and min_start > board[y][x]:
                    min_start = board[y][x]
                elif temp > max_cnt:
                    min_start = board[y][x]
                max_cnt = temp
    print('#%d %d %d' %(ro + 1, min_start, max_cnt))
