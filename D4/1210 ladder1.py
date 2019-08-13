near = [(0,-1), (0,1), (-1,0)]
def ladder_orgi(y,x,ladder):

    if y != 1:
        for dy,dx in near:
            if y + dy == 0:
                return x
    
    if x == 99:
        for dy,dx in [(0,-1), (-1,0)]:
            if ladder[y+dy][x+dx] == 1:
                ladder[y][x] = 3
                return ladder_orgi(y+dy, x+dx,ladder)
    
    if x == 0:
        for dy,dx in [(0,1), (-1,0)]:
            if ladder[y+dy][x+dx] == 1:
                ladder[y][x] = 3
                return ladder_orgi(y+dy, x+dx,ladder)

    for dy,dx in near:
        if ladder[y+dy][x+dx] == 1:
            ladder[y][x] = 3
            return ladder_orgi(y+dy, x+dx,ladder)

for rounds in range(1,11):
    ladder = []
    ro = int(input())
    for i in range(100):
        ladder.append(list(map(int,input().split())))
    
    for i in range(100):
        if ladder[99][i] == 2:
            exit_index = i
    print(f'#{rounds} {ladder_orgi(99,exit_index,ladder)}')
