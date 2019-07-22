for rounds in range(int(input())):
    N, C = map(int,input().split())
    menus = []

    for i in range(N):
        menus.append(list(map(int,input().split())))
    menus.sort(key=lambda menu: menu[1],reverse=True)
    print(menus)
