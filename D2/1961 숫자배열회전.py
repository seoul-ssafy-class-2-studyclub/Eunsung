import copy

def daching(goal_board):
    board_180 = copy.deepcopy(goal_board)
    board_180.reverse()
    for i in range(N):
        board_180[i].reverse()
    return board_180

for rounds in range(int(input())):
    
    N = int(input())
    
    goal_board = []
    for i in range(N):
        goal_board.append(list(input().split()))

    #90도회전
    board_90 = list(map(list,zip(*goal_board)))
    for i in range(N):
        board_90[i].reverse()

    board_180 = daching(goal_board)

    #270도회전 (90도를 180도)
    board_270 = daching(board_90)

    result = list(map(list,zip(board_90, board_180, board_270)))

    print(f'#{rounds + 1}')

    for i in range(N):
        for j in range(3):
            print(''.join(result[i][j]), end = ' ')
        print('')
        