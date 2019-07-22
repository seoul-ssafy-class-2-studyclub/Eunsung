DAYS = {
    0 : 0, 1 : 31, 2 : 29, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31
}

for rounds in range(int(input())):
    m1, d1 = map(int, input().split())

    days = 0

    if m1 == 1 :
        days = d1
    
    else :

        days += d1
        for months in range(2, m1 + 1):
            days += DAYS[months - 1]

    result = (3 + days) % 7

    print(f'#{rounds + 1} {result}')
        