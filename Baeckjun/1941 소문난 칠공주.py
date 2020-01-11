near = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(arr):
    global cnt

    if len(arr) == 7:
        if dp.get(temp_key) != None:
            return 0
        temp_cnt = 0
        temp_key = 0
        for y, x in arr:
            temp_key = temp_key | (1 << (y * 5 + x))
            if soms[y][x]:
                temp_cnt += 1
        
        if temp_cnt >= 4:
            dp[temp_key] = 1
            cnt += 1
            # print(arr)
        return
    
    if len(arr) == 4:
        temp_cnt = 0
        temp_key = 0
        if dp.get(temp_key) == 0:
            return 0
        for y, x in arr:
            temp_key = temp_key | (1 << y * 5 + x)
            if soms[y][x]:
                temp_cnt += 1
        if not temp_cnt:
            dp[temp_key] = 0
            return

    for y, x in arr:
        for dy, dx in near:
            ry = dy + y
            rx = dx + x
            if 0 <= ry < 5 and 0 <= rx < 5 and (ry, rx) not in arr:
                bfs(arr + [(ry, rx)])
     

board = [0] * 5
soms = [[False] * 5 for _ in range(5)]
for y in range(5):
    board[y] = input()

    for x in range(5):
        if board[y][x] == 'S':
            soms[y][x] = True

dp = dict()
cnt = 0
for y in range(5):
    for x in range(5):
        # if y + x >= 5 or y == 4 or x == 4:
        # if y + x >= 5:
        #     continue
        start = (y, x)
        bfs([start])

print(cnt)