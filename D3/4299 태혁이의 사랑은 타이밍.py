for rounds in range(int(input())):
    d, h, m = map(int,input().split())

    d, h, m = (d - 11), (h - 11), (m - 11)

    if d < 0:
        result = -1
    elif d == 0 and h < 0:
        result = -1
    elif d == 0 and h == 0 and m < 0:
        result = -1
    else:
        while h < 0 or m < 0:
            if h < 0:
                h += 24
                d -= 1
            if m < 0:
                m += 60
                h -= 1

        result = d * 60 * 24 + h * 60 + m

    print(f'#{rounds + 1} {result}')    

    
