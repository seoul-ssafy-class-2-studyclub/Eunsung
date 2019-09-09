dic = {
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9,
}

for ro in range(int(input())):
    N, M = map(int,input().split())
    board = []
    for y in range(N):
        board.append(list(map(int,input())))
        if board[-1].count(1):
            check = y
    
    end_idx = 0
    start_idx = 0
    for x in range(M - 1, -1, -1):
        if board[check][x] == 1:
            end_idx = x
            start_idx = x - 55
            break
    
    code = board[check][start_idx:end_idx + 1]
    nums = []
    for idx in range(len(code)):
        if not idx % 7:
            nums.append([])
        nums[-1].append(str(code[idx]))
    res = []
    for num in nums:
        res.append(dic[''.join(num)])

    if not ((res[0] + res[2] + res[4] + res[6]) * 2 + sum(res)) % 10:
        result = sum(res)
    else:
        result = 0

    print('#%d %d' %(ro + 1, result))


