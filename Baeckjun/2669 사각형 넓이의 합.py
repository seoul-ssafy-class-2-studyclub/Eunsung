import sys
sys.stdin = open('input.txt', 'r')

rectangles = []
for i in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    rectangles.append([(x1, y1), (x2, y2)])

min_y, max_y = 100, 0
min_x, max_x = 100, 0
for rectangle in rectangles:
    if rectangle[0][0] < min_x:
        min_x = rectangle[0][0]
    if rectangle[0][1] < min_y:
        min_y = rectangle[0][1]

    if rectangle[1][0] > max_x:
        max_x = rectangle[1][0]
    if rectangle[1][1] > max_y:
        max_y = rectangle[1][1]
board = [[0 for _ in range(max_x + 2)] for _ in range(max_y + 2)]
# print(min_x,min_y,'우와',max_x,max_y)
# print(board)
count = 0
for rectangle in rectangles:
    for y in range(rectangle[0][1], rectangle[1][1]):
        for x in range(rectangle[0][0], rectangle[1][0]):
            if board[y][x] == 0:
                board[y][x] = 1
                count += 1
print(count)
