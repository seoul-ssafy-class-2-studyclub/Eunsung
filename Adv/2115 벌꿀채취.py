for ro in range(int(input())):
    N, M, C = map(int,input().split())
    board = [0] * N
    for y in range(N):
        board[y] = list(map(int,input().split()))
