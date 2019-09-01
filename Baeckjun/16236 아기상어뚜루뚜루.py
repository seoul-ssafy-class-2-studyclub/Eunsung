near = [(-1, 0), (0, -1), (0, 1), (1, 0)]
from pprint import pprint
N = int(input())
bowl = []
now_eat = 0
now_size = 2
time = 0

for y in range(N):
    bowl.append(list(map(int,input().split())))
    for x in range(N):
        if bowl[y][x] == 9:
            shark = (y, x)
            bowl[y][x] = 0
queue = [(shark, 0)]
visited = [[False for _ in range(N + 1)] for _ in range(N + 1)]
before = 0
while queue:
    
    now_lo, t = queue.pop(0)
    y, x = now_lo

    for dy, dx in near:
        ry = y + dy
        rx = x + dx


        if 0 <= ry < N and 0 <= rx < N:

            if visited[ry][rx] or bowl[ry][rx] > now_size:
                continue


            elif bowl[ry][rx] and bowl[ry][rx] < now_size:
                visited = [[False for _ in range(N + 1)] for _ in range(N + 1)]
                shark = (ry, rx)
                now_eat += 1
                if now_eat == now_size:
                    now_size += 1
                    now_eat = 0
                bowl[ry][rx] = 0
                queue = []
                time = t + 1
                queue.append((shark, time))
                pprint(bowl)
                print(time)
                break
            else:
                visited[ry][rx] = True
                queue.append(((ry, rx), t + 1))
    queue.sort(key=lambda x: x[0][0])
    queue.sort(key=lambda x: x[1])
    print(queue)
    print(now_size)
    
print(time)

print(now_size)
print(now_eat)

                
            
        