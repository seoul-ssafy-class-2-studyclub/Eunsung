for rounds in range(int(input())):

    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    moneys_num = [0, 0, 0, 0, 0, 0, 0, 0]
    
    don = int(input())

    for grade in range(8):
        while don >= moneys[grade]:
            don -= moneys[grade]
            moneys_num[grade] += 1
    
    moneys_num = list(map(str,moneys_num))
    print(f'#{rounds+1}')
    print(' '.join(moneys_num))
