import sys
sys.stdin = open('input.txt', 'r')

def check_babies(num):

    if cb_cache[num] != -1:
        return cb_cache[num]
    
    my_sons = []
    haveson = False
    for i in range(1, P + 1):
        if relations[num][i]:
            my_sons.append(i)
            haveson = True

    if not haveson:
        return 0

    res = 0
    for i in my_sons:
        if relations[num][i]:
            res = max(res, check_babies(i) + 1)
    
    cb_cache[num] = res
    return res


# result_list = []
for round in range(1,11):
    P, R = map(int,input().split())
    dot_row = list(map(int,input().split()))
    # dots = []
    relations = [[0 for _ in range(P+1)] for _ in range(P+1)]
    for i in range(R):
        # dots.append((dot_row[i*2], dot_row[i*2 + 1]))
        relations[dot_row[i*2]][dot_row[i*2 + 1]] = 1
    # print(relations)
    cb_cache = [-1 for _ in range(P + 1)]

    sons = [-1 for _ in range(P + 1)]
    for i in range(1, P + 1):
        sons[i] = check_babies(i)
    
    work_sequence = list(map(str,range(1,P+1)))
    work_sequence.sort(key = lambda x: sons[int(x)], reverse= True)
    print('#%d %s' %(round, ' '.join(work_sequence)))
