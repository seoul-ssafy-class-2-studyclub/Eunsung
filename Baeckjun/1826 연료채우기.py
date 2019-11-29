from heapq import heappop, heappush

N = int(input())
info = []
board = [0] * 1000001
for _ in range(N):
    a, b = map(int,input().split())
    board[a] = b

dis, fuel = map(int,input().split())
now = 0
flag = 0
cnt = 0
queue = []

while fuel:
    if now + fuel >= dis:
        break

    for walk in range(1, fuel + 1):
        if board[now + walk]:
            heappush(queue, -board[now + walk])
    
    now += fuel
    fuel = 0
    if now >= dis:
        break
    else:
        if queue:
            fuel += -heappop(queue)
        else:
            flag = 1
            break
    cnt += 1

if flag:
    cnt = -1
print(cnt)
    