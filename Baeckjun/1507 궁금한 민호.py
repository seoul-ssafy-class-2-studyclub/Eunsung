from heapq import heappop, heappush

def findroute(start, goal, route):
    global flag

    if real_board[start][goal]:
        route = route + real_board[start][goal]
        if board[y][goal] == route:
            return True
        elif board[y][goal] > route:
            flag = True
            return True

    for nxt in adj[start]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        if findroute(nxt, goal, route + real_board[start][nxt]):
            visited[nxt] = False
            return True
        visited[nxt] = False

    return False

result = 0
N = int(input())
board = [0] * N
queue = []
visited = [False] * N
real_board = [[0] * N for _ in range(N)] 
adj = [[] for _ in range(N)]

for y in range(N):
    board[y] = list(map(int,input().split()))
    for x in range(y + 1, N):
        heappush(queue, (board[y][x], y, x))

flag = False
while queue:
    if flag:
        break
    dis, y, x = heappop(queue)

    visited[y] = True
    if findroute(y, x, 0):
        visited[y] = False
        continue 
    
    else:
        visited[y] = False
        real_board[y][x] = dis
        real_board[x][y] = dis
        adj[y].append(x)
        adj[x].append(y)
        result += dis

if flag:
    result = -1

print(result)