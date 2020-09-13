def solution(orders, course):
    answer = []

    len_order = len(orders)
    tmp_oders = [0] * len_order

    for i in range(len_order):

        for c in orders[i]:
            tmp_oders[i] += (1 << (ord(c) - ord('A')))
    res = {}

    def combination(before, n, goal, menu):
        if n == goal:
            for tmp_order in tmp_oders:
                tmp_bit = tmp_order & menu
                if menu & tmp_bit == menu:
                    if res.get(goal):
                        if res[goal].get(menu):
                            res[goal][menu] += 1
                        else:
                            res[goal][menu] = 1
                    else:
                        res[goal] = {}
                        res[goal][menu] = 1

            return
        
        for i in range(before + 1, 26):
            combination(i, n + 1, goal, menu + (1 << i))
    answer = []

    def btc(binary):
        res = ''
        for i in range(26):
            if binary & (1 << i):
                res = chr(i + ord('A')) + res
        return res

    for c in course:
        combination(-1, 0, c, 0)
        if res.get(c): max_cnt = max(res[c].values())
        else: break
        
        if max_cnt < 2:
            break
        for k, v in res[c].items():
            if max_cnt == v and max_cnt > 1:
                t = ''.join(sorted(btc(k)))
                answer.append(t)
        
    answer =  sorted(answer)
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]	))