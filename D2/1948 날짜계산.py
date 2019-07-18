DAYS = {
    1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31
}

for rounds in range(int(input())):
    m1, d1, m2, d2 = map(int, input().split())

    days = 0

    if m2 == m1 :
        days = d2 - d1 + 1
    
    else :
        days += DAYS[m1] - d1
        days += d2 + 1
        for months in range(m1 + 1, m2):
            days += DAYS[months]

    print(f'#{rounds + 1} {days}')
        