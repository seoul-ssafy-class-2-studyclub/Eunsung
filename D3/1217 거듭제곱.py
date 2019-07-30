def jegop(x, n):
    if n == 1:
        return x
    return x * jegop(x, n - 1)

for rounds in range(1,11):
    ro = int(input())
    x, n = map(int,input().split())

    print(f'#{rounds} {jegop(x, n)}')
