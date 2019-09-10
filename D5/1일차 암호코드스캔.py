dic = {
    (3,2,1,1):0,
    (2,2,2,1):1,
    (2,1,2,2):2,
    (1,4,1,1):3,
    (1,1,3,2):4,
    (1,2,3,1):5,
    (1,1,1,4):6,
    (1,3,1,2):7,
    (1,2,1,3):8,
    (3,1,1,2):9,
}

for ro in range(int(input())):
    N, M = map(int,input().split())
    board = []
    for y in range(N):
        board.append(input())
    min_0 = M
    for y in range(N):
        temp = board[y].count('0')
        if temp != M and temp < min_0 :
            min_0 = temp
            check = y
        
    codes = ['']
    for x in range(M):
        if board[check][x] == '0' and codes[-1] != '':
            codes.append('')
        if board[check][x] != '0':
            codes[-1] += board[check][x]
    print(codes)
    res_codes = []
    result = 0
    for x in range(len(codes)):
        if codes[x] != '':
            res_codes.append(format(int(codes[x], 16), 'b'))

            for i in range(len(res_codes[-1]) - 1, -1, -1):
                if res_codes[-1][i] != '0':
                    ck = i
                    break
            res_codes[-1] = res_codes[-1][:ck + 1]
            C = len(res_codes[-1]) // 56 + 1
            for j in range(56 * C - len(res_codes[-1])):
                res_codes[-1] = '0' + res_codes[-1]
    temp = [[] for _ in range(len(res_codes))]
    for idx in range(len(res_codes)):
            
        cnt = 1
        for c in range(1, len(res_codes[idx])):
            if not c % (C * 7):
                temp[idx].append([])
                cnt = 1
                continue
            if res_codes[idx][c] == res_codes[idx][c - 1]:
                cnt += 1
            else:
                temp[idx][-1].append(cnt)
                cnt = 1
            if c % (C * 7) == (C * 7) - 1:
                temp[idx][-1].append(cnt)
                cnt = 1
            # for 
        

                
        
    print(res_codes)
    print(temp)
    
    
