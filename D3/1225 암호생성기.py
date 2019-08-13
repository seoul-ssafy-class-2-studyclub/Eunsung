result_list = []
for round in range(1,11):
    N = int(input())
    numbers = list(map(int,input().split()))
    #########################################################
    now = 0
    result = []


    while not 0 in numbers:
        for i in range(1,6):
            numbers[now % 8] -= i
            if numbers[now % 8] <= 0:
                numbers[now % 8] = 0
                now += 1
                break
            now += 1
    
    for i in range(8):
        result.append(str(numbers[(now + i)  % 8]))
    ########################################################
    result_list.append('#%d %s' %(round, ' '.join(result)))
for value in result_list:
    print(value)
    