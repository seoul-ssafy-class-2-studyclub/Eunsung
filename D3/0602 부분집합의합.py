result = []
numbers = list(range(1, 13))
max_num = 2 ** 12 - 1
for round in range(int(input())):
    N, K = map(int,input().split())
    
    
    count = 0

    for i in range(1 << 12):
        bubun = []
        for j in range(12):
            if i & (1 << j):
                bubun.append(numbers[j])
        if sum(bubun) == K and len(bubun) == N:
                count += 1
    result.append('#%d %d' %(round + 1, count))
for value in result:
    print(value)