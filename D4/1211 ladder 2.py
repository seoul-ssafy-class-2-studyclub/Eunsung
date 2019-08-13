def ladder_go(x):
    count = 0
    for i in range(100):
        count += 1

        if x < 99 and ladder[i][x+1] == 1:
            while x < 99 and ladder[i][x+1] == 1:
                x += 1
                count += 1
            
        elif x > 0 and ladder[i][x-1] == 1:
            while x > 0 and ladder[i][x-1] == 1:
                x -= 1
                count += 1
    
    return count

result_list = []
for round in range(1,11):
    ro = int(input())

    ladder = []

    for _ in range(100):
        ladder.append(list(map(int,input().split())))

    start_indexes = []

    for i in range(100):
        if ladder[0][i]:
            start_indexes.append(i)
    # print(start_indexes)

    result_count = 10000
    result_x = 0
    for i in range(len(start_indexes)):
        temp = ladder_go(start_indexes[i])
        if result_count > temp:
            result_x = start_indexes[i]
            result_count = temp

    result_list.append('#%d %d' %(round, result_x))
for value in result_list:
    print(value)

