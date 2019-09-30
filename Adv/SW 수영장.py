def dfs(idx, fee):
    global min_fee

    if idx >= 12:
        if fee < min_fee:
            min_fee = fee
        return
    
    if cache[idx] != -1:
        if cache[idx] > fee:
            return
        else:
            cache[idx] = fee
    if plan[idx] == 0:
        dfs(idx + 1, fee)
    else:
        dfs(idx + 1, fee + plan[idx] * fees[0])
        dfs(idx + 1, fee + fees[1])
        dfs(idx + 3, fee + fees[2])
        dfs(idx + 12, fee + fees[3])

for ro in range(int(input())):
    fees = list(map(int,input().split()))
    plan = list(map(int,input().split()))

    cache = [-1] * 13
    min_fee = 99999 
    dfs(0, 0)
    print('#%d %d' %(ro + 1, min_fee))