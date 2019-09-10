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
def makebi(M):
    M = M.replace('0','0000')
    M = M.replace('1','0001')
    M = M.replace('2','0010')
    M = M.replace('3','0011')
    M = M.replace('4','0100')
    M = M.replace('5','0101')
    M = M.replace('6','0110')
    M = M.replace('7','0111')
    M = M.replace('8','1000')
    M = M.replace('9','1001')
    M = M.replace('A','1010')
    M = M.replace('B','1011')
    M = M.replace('C','1100')
    M = M.replace('D','1101')
    M = M.replace('E','1110')
    M = M.replace('F','1111')
    return M
for ro in range(int(input())):
    N, M = map(int,input().split())
    board = []
    ex_code = []
    codes = []
    total_code = []
    
    for y in range(N):
        co = input()
        co = makebi(co)
        res_codes = []
        idx = len(co) - 1
        temp = [0, 0, 0, 0]

        while idx >= 0:
            if len(res_codes) == 8:
                res_codes.reverse()
                if not res_codes in total_code:
                    total_code.append(res_codes)
                    res_codes = []
            if co[idx] == '0':
                idx -= 1
                continue

            while co[idx] == '1':
                temp[3] += 1
                idx -= 1
            while co[idx] == '0':
                temp[2] += 1
                idx -= 1
            while co[idx] == '1':
                temp[1] += 1
                idx -= 1
            
            temp_sum = sum(temp)
            C = min(temp[1:4])
            temp[0] = (7 * C) - temp_sum
            
            idx -= temp[0]

            temp[3] = temp[3] // C
            temp[2] = temp[2] // C
            temp[1] = temp[1] // C
            temp[0] = temp[0] // C

            res_codes.append(temp)
            temp = [0, 0, 0, 0]

            
    result = 0
    temp = [[[]] for _ in range(len(total_code))]
    for idx in range(len(total_code)):    
        temp_res = []
        for i in range(8):
            temp_res.append(dic[tuple(total_code[idx][i])])
        
        if not ((temp_res[0] + temp_res[2] + temp_res[4] + temp_res[6]) * 2 + sum(temp_res)) % 10:
            result += sum(temp_res)


    
    # for x in range(len(codes)):
    #     if codes[x] != '':
    #         res_codes.append(format(int(codes[x], 16), 'b'))

    #         for i in range(len(res_codes[-1]) - 1, -1, -1):
    #             if res_codes[-1][i] != '0':
    #                 ck = i
    #                 break
    #         res_codes[-1] = res_codes[-1][:ck + 1]
    #         C = len(res_codes[-1]) // 56 + 1
    #         for j in range(56 * C - len(res_codes[-1])):
    #             res_codes[-1] = '0' + res_codes[-1]



    # temp = [[[]] for _ in range(len(res_codes))]
    # for idx in range(len(res_codes)):
            
    #     cnt = 1
    #     for c in range(1, len(res_codes[idx])):
    #         C = len(res_codes[idx]) // 56
    #         if not c % (C * 7):
    #             temp[idx].append([])
    #             cnt = 1
    #             continue
    #         if res_codes[idx][c] == res_codes[idx][c - 1]:
    #             cnt += 1
    #         else:
    #             temp[idx][-1].append(cnt // C)
    #             cnt = 1
    #         if c % (C * 7) == (C * 7) - 1:
    #             temp[idx][-1].append(cnt // C)
    #             cnt = 1
    #     temp_res = []
    #     for i in range(8):
    #         temp_res.append(dic[tuple(temp[idx][i])])
        
    #     if not ((temp_res[0] + temp_res[2] + temp_res[4] + temp_res[6]) * 2 + sum(temp_res)) % 10:
    #         result += sum(temp_res)

    print('#%d %d' %(ro + 1, result))
        

