def counting(now_y, sums):
    global min_sums
    if now_y == N:
        if sums < min_sums:
            min_sums = sums
        return
    
    if sums > min_sums:
        return

    for fct in range(N):
        if vistied[fct]:
            continue
        vistied[fct] = True
        counting(now_y + 1, sums + board[now_y][fct])
        vistied[fct] = False


for ro in range(int(input())):
    N = int(input())
    board = [0] * N
    for y in range(N):
        board[y] = list(map(int,input().split()))
    
    min_sums = 99999
    vistied = [False] * N
    counting(0, 0)
    print('#%d %d' %(ro + 1, min_sums))
