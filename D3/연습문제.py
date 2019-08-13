def go(ls, x, y, look=2):
    global cnt
    cnt += 1
    nxt2 = [[0, 1],[0, -1],[1, 0]]
    nxt0 = [[0, 1], [1, 0]]
    nxt1 = [[0, -1], [1, 0]]
    if look == 2:
        fr = 0
        for a, b in nxt2:
            if 0 <= x+a < 100 and 0 <= y+b < 100:
                if ls[x+a][y+b] == '2':
                    return 1
                elif ls[x+a][y+b] == '1':
                    if go(ls, x+a, y+b, fr) == 1:
                        return 1
            fr += 1
        return 0
    if look == 1:
        fr = 1
        for a, b in nxt1:
            if 0 <= x+a < 100 and 0 <= y+b < 100:
                if ls[x+a][y+b] == '2':
                    return 1
                elif ls[x+a][y+b] == '1':
                    if go(ls, x+a, y+b, fr) == 1:
                        return 1
            fr += 1
        return 0
    if look == 0:
        fr = 0
        for a, b in nxt0:
            if 0 <= x+a < 100 and 0 <= y+b < 100:
                if ls[x+a][y+b] == '2':
                    return 1
                elif ls[x+a][y+b] == '1':
                    if go(ls, x+a, y+b, fr) == 1:
                        return 1
            fr += 2
        return 0
    return 0

for T in range(10):
    ladder = []
    n = int(input())
    for i in range(100):
        ladder.append(input().split())
    start = []
    for j in range(len(ladder[0])):
        if ladder[0][j] == '1':
            start.append([0, j])
    result = []
    for x, y in start:
        cnt = 0
        if go(ladder, x, y) == 1:
            result.append([y,cnt])
    result = sorted(result, key=lambda x:x[1])
    print(f'#{T+1} ',end='')
    print(result[0][0])