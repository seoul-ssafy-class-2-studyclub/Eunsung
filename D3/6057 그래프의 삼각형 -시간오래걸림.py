for rounds in range(int(input())):
    N, M = input().split()

    sun = []
    for i in range(int(M)):
        sun.append(set(input().split()))

    leng = len(sun)

    points = [sun[x]|sun[y]|sun[z] for x in range(0,leng) for y in range(x+1,leng) for z in range(y+1, leng) if len(sun[x]|sun[y]|sun[z]) == 3 ]

    print(f'#{rounds + 1} {len(points)}')
