from itertools import combinations

for rounds in range(int(input())):
    N, C = map(int,input().split())
    menus = []
    for i in range(N):
        tem_p , tem_c = map(int,input().split())
        menus.append((tem_c, tem_p))
    menus = sorted(menus)

    cals = 0
    for menu in menus:
        cals += menu[0]
        if cals > C:
            case_num = menus.index(menu)
            break
    points = [menus[l][1] for l in range(N)]

    for i in range(2, case_num + 1):
        points += [sum(list(zip(*combination))[1]) for combination in combinations(menus,i) if sum(list(zip(*combination))[0]) <= C]


    print(f'#{rounds + 1} {max(points)}')
