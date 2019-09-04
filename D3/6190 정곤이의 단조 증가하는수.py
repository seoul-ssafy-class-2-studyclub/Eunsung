result = []
for rounds in range(int(input())):
    N = int(input())
    numbers = list(map(int,input().split()))
    times = set(numbers[x]*numbers[y] for x in range(N - 1) for y in range(x + 1, N))
    
    max_danjo = -1

    for number in times:
        check = True
        number = str(number)
        for i in range(len(number) - 1):
            if number[i] > number[i + 1]:
                check = False
                break
        if check:
            number = int(number)
            if max_danjo < number:
            	max_danjo = number

    result.append('#%d %d' %(rounds + 1, max_danjo))

for value in result:
    print(value)

