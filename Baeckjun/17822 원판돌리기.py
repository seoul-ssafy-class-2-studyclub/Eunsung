dys = [1,-1,0,0]
dxs = [0,0,1,-1]

def circleOfLife():
    for circle in range(1, N + 1):
        circles[circle] = circles[circle][indexs[circle]:] + circles[circle][:indexs[circle]]
    

def circleMove(circle):
    indexs[circle] += direction[d] * k
    indexs[circle] %= M


def checkSames():
    global count
    locations = set()
    flag = 0
    sums = 0
    # print(circles)
    for y in range(1, N + 1):
        for x in range(M):
            if circles[y][x] == 0:
                continue
            sums += circles[y][x]

            for i in range(4):
                dy, dx = dys[i], dxs[i]
                ry = y + dy
                rx = (x + dx) % M
                if 1 <= ry < N + 1 and circles[y][x] == circles[ry][rx] :
                    flag = 1
                    locations.add((y, x))
                    locations.add((ry, rx))

    if flag:
        count -= len(locations)
        for y, x in locations:
            sums -= circles[y][x]
            circles[y][x] = 0
            
    else:
        if sums % count == 0:
            avg = sums // count
        else:
            avg = sums / count
        # print(avg)
        for y in range(1, N + 1):
            for x in range(M):
                if circles[y][x] == avg or circles[y][x] == 0:
                    continue
                elif circles[y][x] > avg:
                    circles[y][x] -= 1
                    sums -= 1

                else:
                    circles[y][x] += 1
                    sums += 1
    return sums


N, M, T = map(int,input().split())
direction= [-1, 1]
circles = [0] *(N + 1)
count = N * M

for i in range(1, N + 1):
    circles[i] = list(map(int,input().split()))

for _ in range(T):
    indexs = [0] * (N + 1)
    x, d, k = map(int,input().split())

    while x <= N:
        circleMove(x)
        x += x

    circleOfLife()
    result = checkSames()
    if result == 0:
        break

# print(circles)
print(result)