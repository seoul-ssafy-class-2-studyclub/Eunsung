for rounds in range(int(input())):

    N, M = map(int,input().split())
    gap = abs(N - M) + 1
    
    Ai = list(map(int,input().split()))
    Bj = list(map(int,input().split()))
    sums = []
    
    if M >= N:
        
        for s in range(gap):
            sum = 0
            for i in range(N):
                sum += (Ai[i] * Bj[i + s])
            sums.append(sum)
        
    else:
        
        for s in range(gap):
            sum = 0
            for j in range(M):
                sum += (Bj[j] * Ai[j + s])
            sums.append(sum)

    print(f'#{rounds + 1} {max(sums)}')      
