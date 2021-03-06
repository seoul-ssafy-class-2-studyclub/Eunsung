def jungwi(i, result):

    go = True

    if tree[i][1]:
        temp = tree[i][1]
        tree[i][1] = False
        go = False
        jungwi(temp, result).append(tree[i][0])

    if tree[i][2]:
        temp = tree[i][2]
        tree[i][2] = False
        go = False
        result = jungwi(temp, result)
    
    if go:
        result.append(tree[i][0])

    return result

for rounds in range(1,11):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    result = []
    
    for i in range(N):
        data = input().split()
        index = int(data[0])
        string = data[1]
        if len(data) > 2:
            son1 = int(data[2])
            if len(data) >3:
                son2 = int(data[3])
            else:
                son2 = False
        else:
            son1 = False
            son2 = False
        
        tree[index] = ([string, son1, son2])

    result = jungwi(1, result)
    
    print(f'#{rounds} {"".join(result)}')