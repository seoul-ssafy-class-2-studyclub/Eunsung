for rounds in range(1,11):
    ro = int(input())
    board = []
    for i in range(100):
        board.append(list(map(int,input().split())))
    board_col = list(zip(*board))

    sums = []
    for i in range(100):
        sums.append(sum(board[i]))
        sums.append(sum(board_col[i]))
    cross = [[],[]]
    for l in range(100):
        cross[0].append(board[l][l])
        cross[1].append(board[99-l][99-l])
    sums.append(sum(cross[0]))
    sums.append(sum(cross[1]))

    print(f'#{rounds} {max(sums)}')
