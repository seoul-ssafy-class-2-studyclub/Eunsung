N = int(input())
rectangles = []
for i in range(N):
    rectangles.append(tuple(map(int,input().split())))

board = [[0 for _ in range(101)] for _ in range(101)]

square = 0
for i in range(N):
    for x in range(rectangles[i][0], rectangles[i][0] + 10):
        for y in range(rectangles[i][1], rectangles[i][1] + 10):
            if not board[x][y]:
                board[x][y] = 1
                square += 1
print(square)