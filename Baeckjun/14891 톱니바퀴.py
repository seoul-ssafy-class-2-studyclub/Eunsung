def rotation(gear, direction):
    if not (0 <= gear < 4):
        return
    if gear > 0:
        
        if gears[gear][(nows[gear] + 4) % 8] != gears[gear - 1][nows[gear - 1] % 8] and not visited[gear - 1]:

            visited[gear - 1] = True
            rotation(gear - 1, direction * - 1)
    if gear < 3:

        if gears[gear][nows[gear] % 8] != gears[gear + 1][(nows[gear + 1] + 4) % 8] and not visited[gear + 1]:
            visited[gear + 1] = True
            rotation(gear + 1, direction * - 1)

    nows[gear] += direction * -1

for ro in range(int(input())):
    gears = [0] * 4
    nows = [2, 2, 2, 2]
    N = int(input())    
    for y in range(4):
        gears[y] = list(map(int,list(input().split())))


    for _ in range(N):
        visited = [False] * 4
        num, direction = map(int,input().split())
        visited[num - 1] = True
        rotation(num - 1, direction)
        
    res = 0
    for gear in range(4):
        if gears[gear][(nows[gear] - 2) % 8] == 1:
            res += 2 ** gear

    print('#%d %d' %(ro + 1, res))
    
