def dfs(now_day, money):

    if now_day >= N:
        return money
    if money > cache_past[now_day]:
        cache_past[now_day] = money
    else:
        return 0
    
    if cache_future[now_day] != -1:
        return cache_past[now_day] + cache_future[now_day]
    

    earn = board[now_day][1]
    day = board[now_day][0]

    future = 0
    
    #넣는다
    if now_day + day <= N:
        future = dfs(now_day + day, money + earn)

    #안넣는다
    future = max(future, dfs(now_day + 1, money))

    cache_future[now_day] = future - money

    return future


N = int(input())
board = [0] * N
for day in range(N):
    board[day] = tuple(map(int,input().split()))

max_money = 0

cache_future = [-1] * N
cache_past = [-1] * N

print(dfs(0,0))