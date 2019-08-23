N = int(input())

fact = [1 for i in range(N + 4)]
for i in range(2, N + 4):
    fact[i] = fact[i - 1] * i

cases = [0 for _ in range(N // 2 + 2)]
cases[0] = 1
for n in range(1, N // 2 + 2):
    for x in range(n // 2 + 1):
        y = n - 2 * x

        cases[n] += fact[y + x] // (fact[x] * fact[y])

seats = [0 for _ in range(N + 2)]

vip_num = int(input())
for _ in range(vip_num):
    vip = int(input())
    seats[vip] = 1

sets = []
cnt = 0
for i in range(1, N + 1):
    if seats[i]:
        sets.append(cnt)
        cnt = 0
        continue
    cnt += 1
sets.append(cnt)

result = 1
for value in sets:
    result *= cases[value]

print(result)


