near = [(0, 0),(0, -1), (-1, 0), (1, 0), (0, 1), (1, -1), (-1, -1), (1, 1), (-1, 1)]

def check(board):
    for i in range(9):
        row_sum = 0
        col_sum = 0
        for j in range(9):
            row_sum += board[i][j]
            col_sum += board[j][i]
        if not (row_sum == 45 and col_sum == 45):
            return False
    for y, x in [(1,1), (4,1), (7,1), (1,4), (4,4), (7,4),(1,7), (4,7), (7,7)]:
        temp_sum = 0
        for dy, dx in near:
            temp_sum += board[y + dy][x + xd]
        if temp_sum != 45:
            return False
    return True


board = []
zeros = [[] for _ in range(9)]
numbers = [0] * 10
putnum = [[] for _ in range(9)]
for y in range(9):
    board.append(list(map(int,input().split())))
    for x in range(9):
        if not board[y][x]:
            zeros[y].append((y, x))
        else:
            numbers[board[y][x]] += 1
    for num in range(1, 10):
        if not numbers[num]:
            putnum[y].append(num)
    numbers = [0] * 10
for idx in range(9):
    if len(putnum[idx]) == 1:
        num = putnum[idx].pop()   
        y, x = zeros[idx].pop()
        board[y][x] = num

for i in range(8, -1, -1):
    if not len(putnum[i]):
        putnum.pop(i)
        zeros.pop(i)


print(board)
print(putnum)
print(zeros)
