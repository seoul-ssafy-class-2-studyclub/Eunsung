N, P, E = map(int,input().split())

def combination(now_idx, left, right, arr, length):
    global result
    if length == P:
        if left <= E <= right:
            result = arr
            return 
        return

    if left >= E or (N - now_idx < P - length):
        return 
    
    for nxt in range(now_idx + 1, N):
        combination(nxt, left + ducks[nxt][0], right + ducks[nxt][1], arr + [nxt], length + 1)
        if result != -1:
            return
        
def combi_2(now_idx, res, res_arr, l ,r):
    global result_list, flag
    if now_idx == P:
        if res == E:
            result_list = res_arr
            flag = 1
        return

    if res >= E:
        return
    temp_r = r - ducks[result[now_idx]][1]
    temp_l = l - ducks[result[now_idx]][0]
    for duck in range(ducks[result[now_idx]][0], ducks[result[now_idx]][1] + 1):
        if E > duck + temp_r:
            continue
        if E < duck + temp_l:
            return
        combi_2(now_idx + 1, res + duck, res_arr + [duck], l, r)
        if flag:
            return

l = r = 0
ducks = []
result = -1
result_list = [0] * P
pri = [0] * N
flag = 0
for _ in range(N):
    ducks.append(tuple(map(int,input().split())))
combination(-1,0,0,[],0)


if result != -1:
    for i in range(P):
        l += ducks[result[i]][0]
        r += ducks[result[i]][1]
    combi_2(0, 0, [], l , r)

    for i in range(P):
        pri[result[i]] = result_list[i]
    
    for i in range(N):
        print(pri[i], end=' ')
else:
    print(-1)