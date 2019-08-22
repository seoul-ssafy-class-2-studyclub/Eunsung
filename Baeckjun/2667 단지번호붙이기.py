near = [(0,-1), (-1,0), (1, 0), (0,1)]
dangi_houses = []
def dangi(y, x):

    for dx, dy in near:
        if 0 <= x + dx < N and 0 <= y + dy < N and houses[y + dy][x + dx] == 1:
            houses[y + dy][x + dx] = 2
            dangi_houses[-1] += 1
            dangi(y + dy, x + dx)


dangisu = 0
N = int(input())
houses = []
for i in range(N):
    houses.append(list(map(int,input())))

for y in range(N):
    for x in range(N):
        if houses[y][x] == 1:
            dangisu += 1
            dangi_houses.append(1)
            houses[y][x] = 2
            dangi(y, x)

dangi_houses.sort()
print(dangisu)
for value in dangi_houses:
    print(value)
