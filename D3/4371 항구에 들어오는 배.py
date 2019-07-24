def check(days, n):
    for l in range(1, n):
        if not (days[n] - 1) % (days[l] - 1):
            return False
    return True



for rounds in range(int(input())):
    N = int(input())
    days = []
    for i in range(N):
        days.append(int(input()))

    count = 1

    for i in range(N-1, 1, -1):
        if check(days, i):
            count += 1

    print(f'#{rounds + 1} {count}')
