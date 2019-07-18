for test_round in range((int(input()))):
    numbers = list(range(1,int(input())+1))

    for each in range(len(numbers)):
        if numbers[each] % 2 == 0:
            numbers[each] *= (-1)

    result = sum(numbers)
    print(f'#{test_round + 1} {result}')