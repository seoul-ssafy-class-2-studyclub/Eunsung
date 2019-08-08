result = []
for round in range(int(input())):
    N, K = map(int,input().split())

    numbers = list(map(int,input().split()))

    length = len(numbers)

    count = 0
    for i in range(1 << length):
        temp = []
        for j in range(length):
            if i & (1 << j):
                temp.append(numbers[j])
        if sum(temp) == K:
            count += 1

    result.append('#%d %d' %(round + 1, count))
for value in result:
    print(value)
