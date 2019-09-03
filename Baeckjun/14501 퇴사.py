def dfs(idx, money):
    
    if idx >= N:
        return money
    
    if cache[idx].get(money) != None:
        return cache[idx].get(money)
    
    
    
    #이거 안할때
    res = dfs(idx + 1, money)

    #할때
    if idx + works[idx][0] <= N:
        res = max(res, dfs(idx + works[idx][0], money + works[idx][1]))

    cache[idx][money] = res

    return res



N = int(input())
works = []
for _ in range(N):
    works.append(tuple(map(int,input().split())))

cache = [{} for _ in range(N + 1)]

result = dfs(0, 0)  

print(result)
