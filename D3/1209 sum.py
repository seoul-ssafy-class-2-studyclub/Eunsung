def my_sum(arr):
    res = 0
    for i in range(len(arr)):
        res += arr[i]
    return res

def my_zip(*arr):
    for i in range(len(arr)):
        for l in range()


for rounds in range(1,11):
    ro = int(input())
    board = []
    for i in range(100):
        board.append(list(map(int,input().split())))
    board_col = list(zip(*board))

    max_result = 0
    for i in range(100):
        if max_result < my_sum(board[i]):
            max_result = my_sum(board[i])
        if max_result < my_sum(board_col[i]):
            max_result = my_sum(board_col[i])
    cross = [[],[]]
    for l in range(100):
        cross[0].append(board[l][l])
        cross[1].append(board[l][99-l])
    if max_result < my_sum(cross[0]):
        max_result = my_sum(cross[0])
    if max_result < my_sum(cross[1]):
        max_result = my_sum(cross[1])

    print(f'#{rounds} {max_result}')
