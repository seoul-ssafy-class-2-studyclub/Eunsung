board = [False, False, True]+[True] * 999998

for i in range(1, len(board)):
    if board[i] == True:
        for l in range(2*i, len(board), i):
            board[l] = False
        print(i, end=' ')

