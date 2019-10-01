def combi(arr, idx, length, honeys):
    if len(arr) == length:
        res = 0
        if sum(arr) <= C:
            for honey in arr:
                res += honey ** 2
        return res

    res = 0
    for nxt in range(idx + 1, M):
        res = max(res, combi(arr + [honeys[nxt]], nxt, length, honeys))
    
    return res

def earn(arr):
    if sum(arr) <= C:
        res = 0
        for honey in arr:
            res += honey ** 2
        return res

    res = 0
    for cnt in range(M - 1, 0, -1):
        res = max(res, combi([], -1, cnt, arr))

    return res

def setting(arr):
    global max_earn
    if len(arr) == 2:
        y1, x1 = arr[0]
        y2, x2 = arr[1]
        temp_earn1 = cache.get((y1, x1))
        temp_earn2 = cache.get((y2, x2))

        if temp_earn1 == None:
            temp_earn1 = earn(board[y1][x1 : x1 + M])
            cache[(y1, x1)] = temp_earn1
        if temp_earn2 == None:
            temp_earn2 = earn(board[y2][x2 : x2 + M])
            cache[(y2, x2)] = temp_earn2
        
        if max_earn < temp_earn1 + temp_earn2:
            max_earn = temp_earn1 + temp_earn2
        return
    
    start_y = 0 if not arr else arr[0][0]

    for y in range(start_y, N):
        for x in range(N - M + 1):
            if not arr:
                setting([(y, x)])
            else:
                if y != arr[0][0]:
                    setting(arr + [(y, x)])
                elif not arr[0][1] <= x < arr[0][1] + M and not x <= arr[0][1] < x + M:
                    setting(arr + [(y, x)])


for ro in range(int(input())):
    N, M, C = map(int,input().split())
    board = [0] * N
    for y in range(N):
        board[y] = list(map(int,input().split()))
    cache = dict()
    max_earn = 0
    setting([])
    print('#%d %d' %(ro + 1, max_earn))