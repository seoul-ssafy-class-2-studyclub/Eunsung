for rounds in range(4):
    rectangles = list(map(int,input().split()))
    
    # board = [[0 for _ in range(max(rectangles[2],rectangles[6]) + 1)] for _ in range(max(rectangles[3],rectangles[7]) + 1)]
    
    result = 0
    # for y in range(rectangles[1], rectangles[3] + 1):
    #     for x in range(rectangles[0],rectangles[2] + 1):
    #         board[y][x] = 1

    points= []

    for y in range(rectangles[5], rectangles[7] + 1):
        count = 0
        for x in range(rectangles[4],rectangles[6] + 1):
            if rectangles[1] <= y <= rectangles[3] and rectangles[0] <= x <= rectangles[2]:
                points.append((x,y))
                count += 1
                if count > 1:
                    break

                

    if len(points) == 1:
        result = 1
    elif len(points) > 1:
        temp_x = set()
        temp_y = set()
        for point in points:
            temp_x.add(point[0])
            temp_y.add(point[1])
        if len(temp_x) > 1 and len(temp_y) > 1:
            result = 3
        else:
            result = 2
    if result == 0:
        result = 'd'
    elif result == 1:
        result = 'c'
    elif result == 2:
        result = 'b'
    else:
        result = 'a'
    print(result)
        