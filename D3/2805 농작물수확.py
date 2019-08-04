near = [(-1,0), (0,-1), (0,1), (1,0)]

class harvest:

    def __init__(self, y, x, value):
        if type(farm[y][x]) != bool:
            result_value.append(value)
            farm[y][x] = False 
            if y != 0 and y != N - 1 and x != 0 and x != N -1:
                for dy, dx in near:
                    if (y + dy, x + dx) in diamond:
                        farm_harv[y + dy][x + dx] = harvest(y + dy, x + dx, farm[y + dy][x + dx])



result = []
for rounds in range(int(input())):
    N = int(input())
    farm = []
    result_value = []
    diamond = []
    start_index = N // 2
    for y in range(N):
        for x in range(N):
            if y <= start_index:
                if start_index - y <= x <= start_index + y:
                    diamond.append((y, x))
            elif y > start_index:
                if start_index - (N - y -1) <= x <= start_index + (N - y - 1):
                    diamond.append((y, x))

    farm_harv = [[[0] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        farm.append(list(map(int,input())))
    
    farm_harv[start_index][start_index] = harvest(start_index, start_index, farm[start_index][start_index])


    result.append(f'#{rounds + 1} {sum(result_value)}')  

for value in result:
    print(value)