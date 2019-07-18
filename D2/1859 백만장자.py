for i in range(int(input())):
    
    money = 0
    j = int(input())    # 필요없음
    cost_list = list(map(int, input().split()))

    while len(cost_list) != 0:

        index_1 = 0
        max_in_list = max(cost_list)
        index_2 = cost_list.index(max_in_list)

        buy_list = cost_list[index_1:index_2]
        spend = sum(buy_list)
        earn = len(buy_list) * max_in_list
        money += earn - spend

        index_1 = index_2 + 1
        cost_list = cost_list[index_1:]

    print(f'#{i + 1} {money}')