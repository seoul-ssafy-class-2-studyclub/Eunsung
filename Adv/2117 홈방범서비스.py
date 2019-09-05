def distance(h, b):
    return abs(h[0] - b[0]) + abs(h[1] - b[1])

for ro in range(int(input())):
    N, M = map(int,input().split())
    houses = []
    board = []
    for y in range(N):
        board.append(list(map(int,input().split())))
        for x in range(N):
            if board[y][x]:
                houses.append((y, x))

    total_sum = len(houses) * M

    max_cnt = 0
    K = 1
    while True:
        fee = K ** 2 + (K - 1) ** 2
        if total_sum - fee < 0:
            break
        
        for y in range(N):
            for x in range(N):
                temp_earn = 0
                temp_cnt = 0
                for house in houses:
                    if distance((y, x), house) < K:
                        temp_earn += M
                        temp_cnt += 1
                
                temp = temp_earn - fee
                if temp >= 0 and temp_cnt > max_cnt:
                    max_cnt = temp_cnt
                    
        K += 1
    
    print('#%d %d' %(ro+ 1, max_cnt))
                                