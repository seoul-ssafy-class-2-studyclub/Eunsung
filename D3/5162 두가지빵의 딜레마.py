for rounds in range(int(input())):
    a, b, c = map(int,input().split())
    print(f'#{rounds + 1} {c // min(a, b)}')