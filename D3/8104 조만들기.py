for rounds in range(int(input())):
    N, K = map(int,input().split())

    group_num = -1
    
    board = []

    for i in range(N * K):
        if i % K == 0:
            board.append([])
            group_num += 1
            board[group_num].append(i+1)
        else:
            board[group_num].append(i+1)
    for i in range(len(board)):
        if i % 2:
            board[i].reverse()

    each_group = list(zip(*board))

    print(f'#{rounds + 1}', end=' ')
    for i in range(K):
        print(sum(each_group[i]), end=' ')
    print('')