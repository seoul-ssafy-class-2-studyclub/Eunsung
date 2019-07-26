def counting(arr):
    points = [(0,0)]

    for i in range(N):
        temp = [arr[i], [0, 0]]
        points.extend([(x[0] + y[0], x[1] + y[1]) for x in temp for y in points if x[1] + y[1] <= C])
        points = list(set(points))
    
    points.sort(reverse=True)
    return points[0][0]

for rounds in range(int(input())):

    N, C = map(int, input().split())
    
    arr = []
    for i in range(N):
        arr.append(list(map(int,input().split())))

    print(f'#{rounds + 1} {counting(arr)}')
