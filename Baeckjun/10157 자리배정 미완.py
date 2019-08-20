w, h = map(int,input().split())

K = int(input())

if K > w * h:
    print(0)

elif K == 1:
    print(1, 1)

else:
    root = ((h + w) ** 2 - 4 * K) ** 0.5

    n = int(((h + w) - root) // 4)

    min_x = 1 + n
    max_x = w - n
    min_y = 1 + n
    max_y = h - n

    x = y = 1 + n
    now = 2 * n * (h + w) - 4 * (n ** 2) + 1
    curve = 0
    
    while True:
        if curve % 4 == 0:
            for i in range(max_y - min_y + 1):
                now += 1
                if now == K:
                    break
                y += 1
        if now != K:
            x += 1
        if now == K:
            print(x, y)

        if curve % 4 == 1:
            for i in range(max_x - min_x + 1):
                now += 1
                if now == K:
                    break
                x += 1
        if now != K:
            y -= 1
        if now == K:
            print(x, y)
            break

        if curve % 4 == 2:
            for i in range(max_y - min_y + 1):
                now += 1
                if now == K:
                    break
                y -= 1
        if now != K:
            x -= 1
        if now == K:
            print(x, y)

        if curve % 4 == 3:
            for i in range(max_x - min_x + 1):
                now += 1
                if now == K:
                    break
                x -= 1
        if now != K:
            y += 1
        if now == K:
            print(x, y)


