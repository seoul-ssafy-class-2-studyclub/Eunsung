for rounds in range(int(input())):
    D, A, B = map(int,input().split())


    board = [False, False, True]+[True]*(B - 2)
    primes = []
    
    for i in range(2, len(board)):
        if board[i] and A <= i <= B and str(D) in str(i):
            primes.append(i)
        for l in range(i, len(board), i):
            board[l] = False
    print(f'#{rounds + 1} {len(primes)}')
