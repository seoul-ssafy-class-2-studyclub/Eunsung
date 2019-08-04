def counting(arr):
    points = [[0,0]]

    for i in range(N):
        temp = [arr[i], [0, 0]]
        
        for key in temp:
            for key2 in points:
                if key[1] + key2[1] <= C:
                    print([key[0]+key2[0], key[1]+key2[1]])
                    points.append([key[0]+key2[0], key[1]+key2[1]])
    
    points.sort(reverse=True)
    return points[0][0]

for rounds in range(int(input())):

    N, C = map(int, input().split())
    
    arr = []
    for i in range(N):
        arr.append(list(map(int,input().split())))

    print(f'#{rounds + 1} {counting(arr)}')
