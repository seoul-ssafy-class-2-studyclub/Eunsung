near = [(0, -1), (-1, 0), (1, 0), (0, 1)]
def gongi(y, x):
    for dx, dy in near:
        if 0 <= y + dy < h and 0 <= x + dx < w and not cheeze[y + dy][x + dx]:
            cheeze[y + dy][x + dx] = 3
            gongi(y + dy, x + dx)

def noka():
    temp = []
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            for dx, dy in near:
                if cheeze[y][x] == 1 and 0 <= y + dy < h and 0 <= x + dx < w and cheeze[y + dy][x + dx] == 3:
                    temp.append((x, y))
                    break
    return temp
    

from pprint import pprint


h, w = map(int,input().split())
cheeze = []

for _ in range(h):
    cheeze.append(list(map(int,input().split())))

gongi(0,0)
time = -1
cnt = 1
temp = []
while cnt > 0:
    

    melt_cheese = noka()
    cnt = len(melt_cheese)
    
    for x, y in melt_cheese:
        cheeze[y][x] = 3
        gongi(y, x)

    temp.append(melt_cheese)
    time += 1

print(time)
print(len(temp[-2]))