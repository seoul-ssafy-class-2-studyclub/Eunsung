import itertools

for rounds in range(int(input())):
    N, K = map(int,input().split())

    scores = list(map(int,input().split()))
    if K != 1:
        sums = [sum(combination) for combination in itertools.combinations(scores,K)]
        result = max(sums)
    else:
        result = max(scores)

    print(f'#{rounds + 1} {result}')