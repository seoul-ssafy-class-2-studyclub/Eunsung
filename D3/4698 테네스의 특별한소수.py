board = [False, False, True]+[True]*(1000001 - 2)

for i in range(2, 1000001):
    if board[i]:
        for l in range(2 * i, len(board), i):
            board[l] = False
for rounds in range(int(input())):
    primes = []
    D, A, B = map(int,input().split())
      
    for i in range(2, B+1):
        if board[i] and A <= i <= B and str(D) in str(i):
            primes.append(i)

    print(f'#{rounds + 1} {len(primes)}')
