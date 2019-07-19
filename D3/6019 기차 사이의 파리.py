for rounds in range(int(input())):
    d, a, b, f = map(int,input().split())

    t = d / (a + b)

    result = f * t

    print(f'#{rounds + 1} {result}')