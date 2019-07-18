for rounds in range(int(input())):

    board = []
    
    N = int(input())
    for i in range(N):
        board.append([])
    
    numbers = list(input().split())
    
    for floor in range(N):
        for index in range(len(numbers)):
            if ((index + 1) / 2 ** floor) % 2 == 1:
                board[N - floor -1].append(numbers[index])
    print(f'#{rounds + 1}', end = ' ')
    for k in range(N):
        print(' '.join(board[k]))
