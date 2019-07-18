T = int(input())

numbers = list(map(str,list(range(1,T+1))))

count = 0
for i in range(T):
    count = numbers[i].count('3') + numbers[i].count('6') + numbers[i].count('9')
    numbers[i] = int(numbers[i])
    if count == 0:
        print(numbers[i], end = ' ')
    elif count >= 0:
        print('-'*count, end = ' ')