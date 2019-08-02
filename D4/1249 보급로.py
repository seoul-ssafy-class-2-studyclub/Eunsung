from pprint import pprint

for rounds in range(int(input())):
    rounds += 1
    N = int(input())
    map_board = []
    for i in range(N):
        map_board.append(list(map(int,input())))
    print(map_board)


    for i in range(N):
        for l in range(i+1):
            if i == l and l == 0:
                map_board[i-l][l] += 0
            elif i == l:
                map_board[i-l][l] += map_board[i-l][l-1]
            elif l == 0:
                map_board[i-l][l] += map_board[i-l-1][l]
            else:
                map_board[i-l][l] += min(map_board[i-l][l-1], map_board[i-l-1][l])

    for i in range(1,N):
        for l in range(N-i):
            map_board[i+l][N-1-l] += min(map_board[i+l-1][N-1-l], map_board[i+l][N-1-l-1])
    
    print(map_board)
    print(f'#{rounds} {map_board[N-1][N-1]}')
    