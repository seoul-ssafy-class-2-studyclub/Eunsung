for rounds in range(int(input())):
    N, C = map(int,input().split())
    points = []
    cal = []
    for i in range(N):
        tem_p , tem_c = map(int,input().split())
        points.append(tem_p)
        cal.append(tem_c)
    for alls in range(2**N):
        binary = list(map(int,list(format(alls,'b').zfill(N))))
        sums = 0
        point = 0
        for l in range(N):
            sums += cal[l] * binary[l]
        if sums <= C:
            point = sum([points[l] * binary[l] for l in range(N)])
            points.append(point)
    print(f'#{rounds + 1} {max(points)}')
