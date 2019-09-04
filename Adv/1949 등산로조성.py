near = [(0, 1), (0, -1), (-1, 0), (1, 0)]
def findroute(y, x, cnt):
    res = cnt
    for dx, dy in near:
        ry = y + dy
        rx = x + dx
        if 0 <= ry < N and 0 <= rx < N:
            if mountains[ry][rx] < mountains[y][x]:
                res = max(res, findroute(ry, rx, cnt + 1))
    
    return res

    
for ro in range(int(input())):
    N, K = map(int,input().split())
    mountains = []
    max_highs = []
    highest = 0
    for y in range(N):
        mountains.append(list(map(int,input().split())))
        for x in range(N):
            temp = mountains[y][x]
            if highest < temp:
                highest = temp
                max_highs = []
                max_highs.append((y, x))
            elif highest == temp:
                max_highs.append((y, x))
    
    max_route = 0
    for y in range(N):
        for x in range(N):
            for k in range(1, K + 1):
                mountains[y][x] -= k
                for hy, hx in max_highs:
                    max_route = max(max_route, findroute(hy, hx, 1))
                mountains[y][x] += k
    
    print('#%d %d' %(ro + 1,max_route))