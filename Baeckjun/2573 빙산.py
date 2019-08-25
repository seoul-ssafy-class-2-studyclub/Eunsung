near = [(0, -1), (-1, 0), (1, 0), (0, 1)]

def melting(y, x):
    if iceberg[y][x] > waters[y][x]:
        iceberg[y][x] -= waters[y][x]
    else:
        iceberg[y][x] = 0
        for dy, dx in near:
            if 0 <= y + dy < H and 0 <= x + dx < W:
                stack.append((y + dy, x + dx))

def findwater(y, x):
    cnt = 0
    for dy, dx in near:
        if 0 <= y + dy < H and 0 <= x + dx < W and not iceberg[y + dy][x + dx]:
            cnt += 1
    waters[y][x] = cnt

def counting(y, x):
    for dy, dx in near:
        if 0 <= y + dy < H and 0 <= x + dx < W and iceberg[y + dy][x + dx] and not countings[y + dy][x + dx]:
            countings[y + dy][x + dx] = 1
            counting(y + dy, x + dx)


H, W = map(int,input().split())

iceberg = []
waters = []
stack = []

for i in range(H):
    iceberg.append(list(map(int,input().split())))
    waters.append([0 for _ in range(W)])

for y in range(H):
    for x in range(W):
        findwater(y, x)

time = 0
while True:
    cnt = 0
    countings = [[0 for _ in range(W)] for _ in range(H)]

    for y in range(1, H - 1):
        for x in range(1, W - 1):
            if iceberg[y][x]:
                
                melting(y, x)

                if not countings[y][x]:
                    cnt += 1
                    counting(y, x)
            if cnt > 2:
                break
        if cnt > 2:
            break
    if cnt > 2:
        break

    for _ in range(len(stack)):
        (cy, cx) = stack.pop()
        waters[cy][cx] += 1
    time += 1

print(time)