results = []

for rounds in range(int(input())):

    scores = list(map(int,input().split()))

    for i in range(len(scores)):
        if scores[i] < 40:
            scores[i] = 40
    result = sum(scores) // len(scores)

    results.append(f'#{rounds + 1} {result}')
print('\n'.join(results))