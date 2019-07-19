for rounds in range(int(input())):
    test_num = input()

    if int(test_num[-1]) % 2 == 0:
        result = 'Even'
    else :
        result = 'Odd'

    print(f'#{rounds + 1} {result}')