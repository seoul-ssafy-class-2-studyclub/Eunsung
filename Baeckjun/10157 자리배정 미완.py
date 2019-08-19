seats_x, seats_y = map(int,input().split())

K = int(input())

min_x = 1
max_x = seats_x
min_y = 1
max_y = seats_y

if K > seats_x * seats_y:
    print(0)

elif K == 1:
    print(1, 1)
else:
    x = y = 1
    now = 1
    curve = 0

    while (max_x - min_x) + (max_y - min_y) < K - now + 1:
        now += (max_x - min_x) + (max_y - min_y)
        min_x += 1
        min_y += 1
        max_x -= 1
        max_y -= 1
        x += 1
        y += 1
        


    while True:
        if curve % 4 == 0:
            while now < K and min_y <= y <= max_y:
                now += 1
                y += 1
        x += 1
        if now == K:
            print(x, y)
            break

        curve += 1
        min_x += 1


        if curve % 4 == 1:
            while now < K and min_x <= x <= max_x:
                now += 1
                x += 1
        y -= 1
        if now == K:
            print(x, y)
            break
        curve += 1
        max_y -= 1



        if curve % 4 == 2:
            while now < K and min_y <= y <= max_y:
                now += 1
                y -= 1
        x -= 1
        if now == K:
            print(x, y)
            break

        curve += 1
        max_x -= 1


        if curve % 4 == 3:
            while now < K and min_x <= x <= max_x:
                now += 1
                x -= 1
        y += 1
        if now == K:
            print(x, y)
            break
        curve += 1
        min_y += 1



