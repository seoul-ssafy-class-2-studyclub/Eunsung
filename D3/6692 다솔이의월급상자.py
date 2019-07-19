for rounds in range(int(input())):
    N = int(input())
    moneys = []
    average = []
    for i in range(N):
        moneys.append(list(map(float,input().split())))
        average.append(moneys[i][0] * moneys[i][1])
    
    print(f'#{rounds + 1} {sum(average)}')
