for test_round in range((int(input()))):
    numbers = list(map(int,input().split()))
    max_num = max(numbers)
    min_num = min(numbers)

    numbers.pop(numbers.index(max_num))
    numbers.pop(numbers.index(min_num))

    result = round(sum(numbers)/len(numbers))
        
    print(f'#{test_round + 1} {result}')