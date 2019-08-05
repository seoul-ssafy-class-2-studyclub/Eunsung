def sack(temp_cap, item):
    if item == N:
        return 0
    
    # 이미 계산된 결과인지 확인한다
    if cache[temp_cap][item] != -1:
        return cache[temp_cap][item]
    
    #안담는경우(무게는 그대로 아이템을 한칸옮긴다)
    res = sack(temp_cap, item + 1)

    #이걸 담는경우(무게를 올려주고, 안담는경우와 비교하여 높은것을 알려준다)
    if temp_cap + goods[item][0] <= cap:
        res = max(res, sack(temp_cap + goods[item][0], item + 1)+goods[item][1])
    
    cache[temp_cap][item] = res
    return res



result = []
for rounds in range(int(input())):
    N, cap = map(int,input().split())
    cache = [[-1 for _ in range(N)] for _ in range(cap + 1)]
    goods = []
    for i in range(N):
        goods.append(tuple(map(int,input().split())))

    result_value = sack(0,0)
    result.append(f'#{rounds + 1} {result_value}')

for value in result:
    print(value)
    

