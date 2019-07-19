for rounds in range(int(input())):
    N, Q = map(int,input().split())

    box = ['0'] * N
    
    for i in range(1,Q+1):
        left, right = map(int,input().split())
        for l in range(left-1,right):
            box[l] = str(i)
    print(f'#{rounds + 1}', end=' ')
    print(' '.join(box))
