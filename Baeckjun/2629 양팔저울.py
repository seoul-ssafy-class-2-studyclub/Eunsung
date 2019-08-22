N = int(input())
choos = list(map(int,input().split()))
K = int(input())
goals = list(map(int,input().split()))

cache = [set() for _ in range(N)]
cache[0].add(0)
cache[0].add(choos[0])

for i in range(1, N):
    for number in cache[i - 1]:
        for x in [number, number - choos[i], number + choos[i]]:

            cache[i].add(x)

result = set()
for i in range(N):
    result.update(cache[i])

for value in goals:
    if value in result:
        print('Y', end=' ')
    elif (-1) * value in result:
        print('Y', end=' ')
    else:
        print('N', end=' ')

