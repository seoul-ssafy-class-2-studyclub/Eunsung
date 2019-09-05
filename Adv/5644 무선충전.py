def permutations(a_bc, b_bc, c):

    if c == 2:
        if a_bc == b_bc:
            return a_bc[3]
        elif b_bc:
            return a_bc[3] + b_bc[3]
        else:
            return a_bc[3]
    res = 0
    for idx in range(len(p_bc[1])):
        res = max(res, permutations(a_bc, p_bc[1][idx], c + 1))

    return res


directions = {0:(0, 0), 1:(0, -1), 2:(1, 0), 3:(0, 1), 4:(-1, 0)}

def route(p, b):
    return abs(p[0] - b[0]) + abs(p[1] - b[1])

for ro in range(int(input())):
    M, BC = map(int,input().split())
    a_move = list(map(int,input().split()))
    b_move = list(map(int,input().split()))
    bc_info = []
    for _ in range(BC):
        bc_info.append(tuple(map(int,input().split())))
    
    bc_info.sort(key=lambda x: x[3], reverse=True)
    a = (1, 1)
    b = (10, 10)
    result = 0
    for _ in range(len(a_move) + 1):

        p = (a, b)
        p_cnt = [0, 0]
        p_bc = [[[0, 0, 0, 0]],[[0, 0, 0, 0]]]
        for bc in bc_info:
            bc_x, bc_y, bc_range, bc_p = bc
            for idx in range(2):
                if route(p[idx], (bc_x, bc_y)) <= bc_range:
                    p_cnt[idx] += 1
                    p_bc[idx].append(bc)
        
        res = 0
        for a_idx in range(len(p_bc[0])):
            a_bc = p_bc[0][a_idx]
            if p_bc[1]:
                res = max(res, permutations(a_bc, [], 1))
        if a_move:
            a_dx, a_dy = directions[a_move.pop(0)]
            b_dx, b_dy = directions[b_move.pop(0)]
            a = (a[0]+a_dx, a[1]+a_dy)
            b = (b[0]+b_dx, b[1]+b_dy)
        result += res
    print('#%d %d' %(ro + 1,result))
        

