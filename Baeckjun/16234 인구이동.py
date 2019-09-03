import sys
sys.setrecursionlimit(10000)
near = [(-1, 0), (0, -1), (0, 1), (1, 0)]
from pprint import pprint
def dfs(y, x):
    global temp_sum
    for dx, dy in near:
        ry = y + dy
        rx = x + dx
        if 0 <= ry < N and 0 <= rx < N:
            if visited[ry][rx]:
                continue
            if L <= abs(nations[ry][rx] - nations[y][x]) <= R:
                visited[ry][rx] =  True
                temp_sum += nations[ry][rx]
                hood[-1].append((ry, rx))
                dfs(ry, rx)

    
N, L, R = map(int,input().split())

nations = []
sums = []
hood = []
visited = [[False for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(N):
    nations.append(list(map(int,input().split())))

time = 0

while True:
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                temp_sum = 0
                flag = 0
                for dx, dy in near:
                    ry = y + dy
                    rx = x + dx 
                    if 0 <= ry < N and 0 <= rx < N:
                        if not visited[ry][rx] and L <= abs(nations[ry][rx] - nations[y][x]) <= R:
                            if not hood or not (y, x) in hood[-1]:
                                hood.append([(y, x)])
                                temp_sum += nations[y][x]
                            visited[y][x] = True
                            visited[ry][rx] = True
                            temp_sum += nations[ry][rx]
                            hood[-1].append((ry, rx))
                            dfs(ry, rx)
                            flag = 1

                if flag:
                    sums.append(temp_sum)

                
    if not hood or not sums:
        break
    while hood:
        temp = hood.pop(0)
        cnt = len(temp)
        sum_s = sums.pop(0)

        for y, x in temp:
            nations[y][x] = sum_s // cnt
            visited[y][x] = False
    time += 1


print(time)
        
