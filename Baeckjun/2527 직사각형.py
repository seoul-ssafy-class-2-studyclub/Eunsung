
for rounds in range(4):
    result = 0
    rectangles = list(map(int,input().split()))
    
    center1 = ((rectangles[0] + rectangles[2]) , (rectangles[1] + rectangles[3]))
    center2 = ((rectangles[4] + rectangles[6]) , (rectangles[5] + rectangles[7]))

    distance = (center1[0] - center2[0]) ** 2 + (center1[1] - center2[1]) ** 2

    sum_x = (rectangles[2] - rectangles[0]) + (rectangles[6] - rectangles[4])
    sum_y = (rectangles[3] - rectangles[1]) + (rectangles[7] - rectangles[5])


    if distance > sum_x ** 2 + sum_y ** 2 or sum_x < abs(center1[0] - center2[0]) or sum_y < abs(center1[1] - center2[1]):
        result = 'd'
    elif distance == sum_x ** 2 + sum_y ** 2:
        result = 'c'
    elif abs(center1[0] - center2[0]) == sum_x or abs(center1[1] - center2[1]) == sum_y:
        result = 'b'
    else:
        result = 'a'

    print(result)
        